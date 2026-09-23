test_cases = int(input())

while test_cases > 0:
    total_components = int(input())

    expected_position = 1
    prev_misplaced_label = 1000000
    can_be_assembled = True

    for label_str in input().split():
        component_label = int(label_str)

        if component_label != expected_position:

            if component_label > prev_misplaced_label:
                can_be_assembled = False

            prev_misplaced_label = component_label

        expected_position += 1

    if can_be_assembled:
        print("YES")
    else:
        print("NO")

    test_cases -= 1
