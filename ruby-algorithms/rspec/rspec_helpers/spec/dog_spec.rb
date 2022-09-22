# helpers are basically ruby methods that we can use in different test case
require_relative '../dog'

describe Dog do
  ## helper method
  def create_and_walk(good_or_bad)
    dog = Dog.new(good_or_bad)
    dog.walk_dog
    return dog
  end

  it 'should be able to create and walk a good dog' do
    dog = create_and_walk(true)

    expect(dog.good_dog).to be truecreate_and_walk
    expect(dog.has_been_walked).to be true
  end

  it 'should be able to create and walk a bad dog' do
    dog =create_and_walk(false)

    expect(dog.good_dog).to be false
    expect(dog.has_been_walked). to be true
  end
end


## Now we can reduce the code to be reusable by create a create_and_walk helper method
