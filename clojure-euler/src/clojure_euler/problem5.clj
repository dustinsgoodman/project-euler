;2520 is the smallest number that can be divided
;by each of the numbers from 1 to 10 without any
;remainder.

;What is the smallest positive number that is
;evenly divisible by all of the numbers from 1
;to 20?

;==> 232792560

(ns clojure-euler.problem5
  (:use clojure.math.numeric-tower))

(defn solve-problem5 []
  (reduce lcm (range 2 21)))
