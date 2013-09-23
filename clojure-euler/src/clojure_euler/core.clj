(ns clojure-euler.core
  (:gen-class))

(use 'clojure-euler.problem1)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  ;; work around dangerous default behaviour in Clojure
  (alter-var-root #'*read-eval* (constantly false))
  (println solve-problem1))
