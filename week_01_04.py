import pandas
import re


def get_first_name_from_miss(name):
    fname = ''
    # print(f'search in name: {name}')
    try:
        fname = re.search(r'Miss\. \w+\b', name).group(0).split(' ')[1]
    except AttributeError:
        # print(f'Miss Error for search in name: {name}')
        return name
    # result = re.search(r'Miss\w{2,18}\b', name)
    # print(f'result of search: {fname}')
    return fname


def get_first_name_from_mrs(name):
    fname = ''
    # print(f'search in name: {name}')
    try:
        fname = re.search(r'Mrs\..+\(\w+\b', name).group(0)
    except AttributeError:
        # print(f'Mrs Error for search in name: {name}')
        return name

    fname = re.search(r'\(\w+', fname).group(0)[1:]
    # print(f'result of search: {fname}')
    return fname


def get_first_name(name_str):
    fname = 'Man'
    # print(f'search in name: {name_str}')

    if 'Mr.' in name_str:
        return 'Man'
    elif 'Miss.' in name_str:
        # print('Founded Miss.')
        fname = get_first_name_from_miss(name_str)
    elif 'Mrs.' in name_str:
        fname = get_first_name_from_mrs(name_str)
    else:
        pass

    return fname


data = pandas.read_csv('titanic.csv', index_col='PassengerId')
data['FirstName'] = 'Man'

first_name_list = []

for index, row in data.iterrows():
    # pass_id = row['PassengerId']
    pass_name = row['Name']
    # first_name = row['FirstName']
    # print(f'Name: {pass_name}, FirstName: {first_name}')
    first_name_list.append(get_first_name(pass_name))
    # row['FirstName'] = get_first_name(pass_name)

first_name = pandas.Series(first_name_list)
most_popular_name = first_name.value_counts()[1:2]
print('Список популярных имен:')
print(most_popular_name)
# print(type(three_most_pop_name))
# three_most_pop_name.iterrows

# for index, val in three_most_pop_name:
#     print(index)
#     print(val)
# print(first_name.value_counts()[:5])
# data['FirstName'] = first_name.values
# print(data[:10])

# woman_name_list = data['FirstName'].value_counts()
# print('Список популярных имен:')
# print(woman_name_list[:10])
# print(woman_name_list[1])
# print(type(woman_name_list))



# first_name = get_first_name('Heikkinen, Miss. Laina')
# print(first_name)
#
# first_name = get_first_name('Futrelle, Mrs. Jacques Heath (Lily May Peel)')
# print(first_name)

# print(data[:10])

# for data['FirstName'] =

# и объединить data и female_data
# result_data = data.merge(female_data, 'right', on='PassengerId')



# print (data[data['Sex'].isin(['female'])].Name[:5])

# data['FirstName'] = data['Name'] + ' + test'
# data['FirstName'] = get_first_name(data['Name'])

# data['FirstName'] = data[data['Sex'].isin(['female'])].Name

# print(data['FirstName'] = get_first_name(data[data['Sex'].isin(['female'])].Name))
# data['FirstName'] = get_first_name(data[data['Sex'].Name)

# print(data[:10])
# print (data[data['Sex'].isin(['female'])].FirstName[:5])

# data['FirstName'] = 'FirstName'
# for row in data.itertuples():
#     if row[4] == 'female':
#         print(row[4])
#         row[12] = 'FirstName'
#         # data['FirstName'] = 'female'
#     else:
#         pass
#         # data['FirstName'] = ''

    # print (row[3])

# print (data[data['Sex'].isin(['female'])].FirstName[:5])
