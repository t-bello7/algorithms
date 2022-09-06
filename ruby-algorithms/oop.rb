#OOP implementatin - Encapsulation, Abstraction, Inheritance, Polymorphism

class Animal
  attr_reader :id, :type, :number_of_legs
  attr_accessor :name
  def initialize(type, number_of_legs, name: "Unknown")
    @id = Random.rand(1..1000)
    @name = name
    @number_of_legs = number_of_legs
    @type = type
  end
  def speak
    "grrrs"
  end
end

class Dog < Animal
  def initialize(color, name:"Unknown")
    super("dog", 4, name )
    @color = color
  end
  def bring_a_stick
    "Here is your stick: -----"
  end
  def speak
    "Woof, woof"
  end
end

class Spider < Animal
  def initialize(web_strength_level, name="Unknown")
    super("spider", 8, name)
    @web_strength_level = web_strength_level
  end
  def make_a_web
    "www"
  end
  def speak
    "...."
  end
end

