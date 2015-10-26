module Toolkit
  def prime?(num)
    return false if num % 2 == 0
    range = (3..((num**0.5)+1).to_i).step(2).to_a
    return false if range.any? { |i| num % i == 0 }
    true
  end

  def range_generator(start, finish, reverse = false)
    range = (start..finish).to_a
    reverse ? range.reverse : range
  end
end
