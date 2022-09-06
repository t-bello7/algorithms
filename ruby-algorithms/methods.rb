class Accounts
  def reading_charge
    puts "read the charge"
  end

  #this way of naming a funtion allows us to access the function without instantiting the class
  def Accounts.return_date
    puts "read todays date"
  end
end

Accounts.return_date()

# giving alias to methods or global variables
# The alias of a method keeps the currrent definition of the method, even when methods are overridden

def bar
  puts "this is bar"
end

alias foo bar

foo

# making a method undefined using undef

undef foo

