from command import rover
from command import validator

if __name__ == '__main__':

    print("Write initial coordinates in the form x,y,direction")
    initial_state_subject = tuple(input().split(","))

    if validator.Validator.subject_is_ok(initial_state_subject):
        receiver = rover.Rover(initial_state_subject)

        while True:
            print("Rover is at position ", receiver.get_state())
            print("Write command:")

            parameters = input()

            if validator.Validator.parameters_are_ok(parameters):
                receiver.move(parameters)


    print("Exiting due to the wrong format")


