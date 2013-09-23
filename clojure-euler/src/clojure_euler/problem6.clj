;The sum of the squares of the first ten natural numbers is,
;1^2 + 2^2 + ... + 10^2 = 385
;The square of the sum of the first ten natural numbers is,
;(1 + 2 + ... + 10)^22 = 55^22 = 3025
;Hence the difference between the sum of the squares of the
;first ten natural numbers and the square of the sum is
;3025 - 385 = 2640.

;Find the difference between the sum of the squares of the
;first one hundred natural numbers and the square of the sum.

;==> 25164150
(ns clojure-euler.problem6)

(defn sumOfNums [n]
  (/ (* n (+ n 1)) 2))

(defn sumOfSquares [n]
  (/ (* n (+ n 1) (+ (* 2 n) 1)) 6))

(defn solve-problem6 []
  (- (Math/pow (sumOfNums 100) 2) (sumOfSquares 100)))
