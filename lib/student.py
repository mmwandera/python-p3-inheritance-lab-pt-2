class Student:

    # Write a method in the Student class, hello(), that print()s out the phrase: "Hey there! I'm so excited to learn stuff."
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    # Write a method in the Student class, raise_hand(), that print()s out the phrase: "Pick me!"
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):

    # Write a method in the ChattyStudent class, hello(), that uses super() to inherit the behavior of the hello() method from the parent class. Then, augment that method to also print() out the very chatty phrase
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    # Write a method in the ChattyStudent class, raise_hand(), that uses super() ten times so that the method will print() out "Pick me!" ten times.
    def raise_hand(self):
        for i in range(0,10):
            print("Pick me!") # OR - super().raise_hand()
        
