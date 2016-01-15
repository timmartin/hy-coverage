import coverage.plugin
import hy.importer
import ast
import os.path

def coverage_init(reg, options):
    """An init callback that is called on initialisation to register the
    classes provided by this plugin.
    """
    reg.add_file_tracer(HyCoveragePlugin())

class HyCoveragePlugin(coverage.plugin.CoveragePlugin):
    """The main entry point for the coverage plugin. This is responsible
    for determining which modules it understands (i.e. all Hy
    modules), and acts as an Abstract Factory to instantiate
    appropriate objects to handle coverage reporting in Hy files.
    """

    # A set of files that can't be parsed using import_file_to_ast(),
    # which we therefore ignore for coverage purposes.
    # TODO: This fails to account for similarly-named files in user
    # code.
    skip = set([
        'shadow.hy'
    ])
    
    def __init__(self):
        super(HyCoveragePlugin, self).__init__()

    def file_tracer(self, filename):
        if filename.endswith('.hy') and \
           (os.path.basename(filename) not in self.skip):
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
            os.path.basename(os.path.splitext(self.filename)[0]))

        hittable_lines = set()
        line_collector = ASTLineCollector(hittable_lines)
        line_collector.visit(ast)
        return hittable_lines
        
