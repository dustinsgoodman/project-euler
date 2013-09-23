(ns clojure-euler.core
  (:gen-class)
  (:use clojure-euler.problem1
        clojure-euler.problem2
        clojure-euler.problem3
        clojure-euler.problem4
        clojure-euler.problem5
        clojure-euler.problem6))



(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ;; work around dangerous default behaviour in Clojure
  (alter-var-root #'*read-eval* (constantly false))
  (time (println (str "Problem 1: " (solve-problem1))))
  (time (println (str "Problem 2: " (solve-problem2))))
  ;(time (println (str "Problem 3: " (solve-problem3))))
  (time (println (str "Problem 4: " (solve-problem4))))
  (time (println (str "Problem 5: " (solve-problem5))))
  (time (println (str "Problem 6: " (solve-problem6))))
  )
