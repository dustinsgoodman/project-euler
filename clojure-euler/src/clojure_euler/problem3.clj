;The prime factors of 13195 are 5, 7, 13 and 29.
;What is the largest prime factor of the number 600851475143?
;==> 6857
(ns clojure-euler.problem3)

(defn factor [n]
  (filter #(= 0 (mod n %)) (range 2 n)))

(defn isPrime? [n]
  (if (= 0 (mod n 2))
    false
    (if (some #(= 0 (mod n %)) (range 3 (+ 1 (int (Math/pow n 0.5)))))
      false
      true
      )))

(defn solve-problem3 []
  (max (filter isPrime? (factor 600851475143))))
