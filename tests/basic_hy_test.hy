(defn function-hit [num]
  (print "hit function with" num)
  (if (= num 100)
    (print "not hit")
    (print "hit")))

(defn function-not-hit []
  (print "this line not hit"))

(function-hit 100)
