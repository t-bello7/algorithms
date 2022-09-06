
## Conditions
x = 1
if x > 2
    puts " x is greater than 2"
elsif x <= 2 and x != 0
    puts "x is 1"
else
    puts " I can't guess the number"
end


## simple if condition modifier
$debug = 1
print "debug\n" if $debug

# unless statement - executes false condition
x = 1
unless x >= 2
    puts "x is less than 2"
else
    puts "x is greater than 2"
end

## simple unless modifier
$var = 1
print "1 -- Value is set\n" if $var
print "2 -- Value is set \n" unless $var

$var = false
print "3 -- Values is set \n" unless $var

$age = 14
case $age
when 0 .. 2
    puts "baby"
when 3 .. 6
    puts "little child"
when 7 .. 12
    puts "child"
when 13 .. 18
    puts "youth"
else
    puts "adult"
end

