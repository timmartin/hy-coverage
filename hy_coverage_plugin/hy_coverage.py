import coverage.plugin
import hy.importer
import ast
import os.path


class HyCoveragePlugin(coverage.plugin.CoveragePlugin):
    """The main entry point for the coverage plugin. This is responsible
    for determining which modules it understands (i.e. all Hy
    modules), and acts as an Abstract Factory to instantiate
    appropriate objects to handle coverage reporting in Hy files.
    """

    def __init__(self):
        super(HyCoveragePlugin, self).__init__()

    def file_tracer(self, filename):
        if filename.endswith('.hy'):
            return HyFileTracer(filename)
        else:
            return None

    def file_reporter(self, filename):
        return HyFileReporter(filename)

    def sys_info(self):
        return []


class HyFileTracer(coverage.plugin.FileTracer):
    """Class for holding metadata about a Hy code file at runtime.
    """

    def __init__(self, filename):
        self.filename = filename
    
    def source_filename(self):
        return self.filename


class ASTLineCollector(ast.NodeVisitor):
    """An AST visitor that collects line numbers that belong to one of the
    nodes in the AST.
    """
    
    def __init__(self, line_set):
        self.line_set = line_set

    def generic_visit(self, node):
        if hasattr(node, 'lineno'):
            self.line_set.add(node.lineno)
        super(ASTLineCollector, self).generic_visit(node)

        
class HyFileReporter(coverage.plugin.FileReporter):
    """This class is used in the analysis phase to provide information
    about hittable lines in a particular Hy module.
    """
    
    def __init__(self, filename):
        super(HyFileReporter, self).__init__(filename)

    def lines(self):
        ast = hy.importer.import_file_to_ast(
            self.filename,
            self.module_name_from_filename(self.filename))

        hittable_lines = set()
        line_collector = ASTLineCollector(hittable_lines)
        line_collector.visit(ast)
        return hittable_lines

    def module_name_from_filename(self, filename):
        directory_name, filename = os.path.split(filename)
        module_name = os.path.splitext(filename)[0]
        while True:
            if (not os.path.exists(os.path.join(directory_name, "__init__.py"))
                and not os.path.exists(os.path.join(directory_name, "__init__.hy"))):
                return module_name
            directory_name, package = os.path.split(directory_name)
            module_name = package + '.' + module_name
