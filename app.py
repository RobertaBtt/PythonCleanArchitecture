from service_layer import services

if __name__ == '__main__':
    robot_list = []
    try:
        upper_right = tuple(input().split(" "))
        area = services.create_area(int(0), int(0), int(upper_right[0]), int(upper_right[1]))

        if area is None:
            print("Check area parameters")
        else:
            while True:
                first_list = tuple(input().split(" "))
                robot = services.create_robot(int(first_list[0]), int(first_list[1]), first_list[2], area)
                if robot is not None:
                    instructions = input()
                    services.send_instructions(robot, instructions)
                    robot_list.append(robot)
                else:
                    print("Robot cannot be deployed, check its coordinates, orientation and area size")
    except Exception as ex:
        pass
    finally:
        if len(robot_list) > 0:
            for robot in robot_list:
                print(robot.position.x, end=" ")
                print(robot.position.y, end=" ")
                print(robot.orientation)

