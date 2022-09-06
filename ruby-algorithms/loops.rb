# each loops
numbers = [1, 3, 5, 7]
numbers.each { |n| puts n }

hash = { bacon: 300, coconut: 200}
hash.each {|key, value| puts "#{key} price is #{value}"}

# each with index loop
animals = ['dog', 'tiger', 'lion']
animals.each_with_index { |animal, id| puts "#{animal} have id of #{id}" }

# times loop
10.times{ |x| puts "I am learning ruby #{x}"}

# range loops
# print a range of items
(2..10).each{|x| puts "Print #{x}"}

# while loop
n = 0
while n <= 10
    puts n
    n += 1
end

# until loop - This is the same as while but the condition is reversed.
bottle = 0
until bottle == 10
    bottle += 1
    puts "bottle #{bottle}"
end

# next keyword skips to the next loop iteration when a condition is met
10.times do |i|
    next unless i.even?
    puts "hello #{i}"
end

# or use select & step instead of next
puts (0...10).select(&:even?)

# stop a loop early before a condition is met, or before you go over all the elements of the collection.
numbers = [1,2,4,9,12]
numbers.each do |n|
  break if n > 10
  puts n
end
