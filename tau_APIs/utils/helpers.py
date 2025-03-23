def obtain_person_by_lastname(unique_last_name, people):
    return [person for person in people if person['lname']
            == unique_last_name]  # new_user va a ser igual a person si lname == unique_last_name, y esto lo prueba para cada person en people
