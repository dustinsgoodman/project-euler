;A palindromic number reads the same both ways. The
;largest palindrome made from the product of two 2-digit
;numbers is 9009 = 91 99.

;Find the largest palindrome made from the product of two
;3-digit numbers.

;==> 906609
(ns clojure-euler.problem4
  (:require [clojure.string :as string]))

(defn palindrome? [x]
  (= (str x) (clojure.string/join (reverse (str x)))))

(defn solve-problem4 []
  (apply max (filter palindrome? (for [x (range 100 1000)
                                     y (range 100 1000)]
                                 (* x y)))))
