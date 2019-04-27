import sys
import json


def read_json_data(filename):
    try:
        with open(filename) as jf:
            json_data = json.load(jf)
    except FileNotFoundError:
        print('Error, specified file not found in current directory!')
        exit(-1)
    except ValueError:
        print('Error, provided file not in correct json format!')
        exit(-1)
    else:
        return json_data


def build_html(json_data):
    html_template = """<!DOCTYPE html>
<html>
<head>
  <title>{full_name}</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <div class="business-card {gender}">
    <h1 class="full-name">{full_name}</h1>
    <img class="avatar" src="avatars/{image_source}">
    <div class="base-info">
      <p>Age: {age}</p>
      <p>Birth date: {birth_date}</p>
      <p>Birth place: {birth_place}</p>
      <p>Gender: {gender}</p>
    </div>
"""
    people_lst = json_data["people"]
    list_of_business_cards = []
    for person in people_lst:
        person_card = parse_basic_info(html_template, person)
        person_card = parse_interests(person_card, person)
        person_card = parse_skills(person_card, person)
        person_card += "</div>\n</body>\n</html>"
        save_business_card(person_card, person, list_of_business_cards)
    return list_of_business_cards


def parse_basic_info(html_template, person):
    basic_info = {
        'full_name': person["first_name"] + ' ' + person["last_name"],
        'gender': person["gender"],
        'image_source': person['avatar'],
        'age': person['age'],
        'birth_date': person["birth_date"],
        'birth_place': person["birth_place"]
    }
    return html_template.format(**basic_info)


def parse_interests(person_card, person):
    if person["interests"]:
        person_card += '\t<div class="interests">\n\t\t<h2>Interests:</h2>\n\t\t<ul>\n'
        for interest in person["interests"]:
            person_card += "\t\t\t<li>{}</li>\n".format(interest)
        person_card += "\t\t</ul>\n\t</div>\n"
        return person_card


def parse_skills(person_card, person):
    if person["skills"]:
        person_card += '\t<div class="skills">\n\t\t<h2>Skills:</h2>\n\t\t<ul>\n'
        for skill in person["skills"]:
            person_card += "\t\t\t<li>{}</li>\n".format(skill["name"] + ' - ' + str(skill["level"]))
        person_card += "\t\t</ul>\n\t</div>\n"
        return person_card


def save_business_card(person_card, person, list_of_business_cards):
    if person_card:
        file_name = person["first_name"] + '.html'
        with open(file_name, 'w+') as html_file:
            html_file.write(person_card)
        list_of_business_cards.append(file_name)


def main(filename):
    people_data = read_json_data(filename)
    created_files = build_html(people_data)
    return created_files


if __name__ == '__main__':
    filename = sys.argv[1]
    print(main(filename))
