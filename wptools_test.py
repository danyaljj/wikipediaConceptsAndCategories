import os

import wptools
from time import sleep


def test():
    page = wptools.page('Donald Trump')
    print(page.get_wikidata())
    print(page.get_wikidata().data["aliases"])


path = 'static/wiki'


def extract_category_members(cat_name, prefix):
    sleep(1)
    cat = wptools.category(cat_name)
    prefix2 = prefix + "/" + cat_name.replace("Category:", "").replace("category:", "").replace(" ", "_")

    if len(prefix2) > 2500:
        return

    members = [x['title'] for x in cat.get_members().data['members'] if "list of" not in x['title'].lower()]
    if len(members) > 2:
        if not os.path.exists(path + prefix):
            os.makedirs(path + prefix)
        with open(path + prefix2 + '.txt', 'w') as f:
            f.write('\n'.join(members))
    if 'subcategories' in cat.get_members().data:
        for c_name in cat.get_members().data['subcategories']:
            extract_category_members(c_name['title'], prefix2)


main_categories = [
    'Category:Nature',
    'Category:Natural sciences',
    'Category:People',
    'Category:Science',
    'Category:Surnames',
    'Category:Personal life',
    'Category:Library science',
    'Category:Research',
    'Category:Culture',
    'Category:Arts',
    'Category:Places',
    'Category:Geography',
    'Category:Health',
    'Category:Healthcare occupations',
    'Category:Events',
    'Category:History',
    'Category:Formal sciences',
    'Category:Thought',
    'Category:Philosophy',
    'Category:Belief',
    'Category:Religion',
    'Category:Social sciences',
    'Category:Society',
    'Category:Applied sciences',
    'Category:Technology'
]


def extract():
    for c in main_categories:
        extract_category_members(c, '')


if __name__ == '__main__':
    # test()
    extract()
