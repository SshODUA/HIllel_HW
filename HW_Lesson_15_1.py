import re

#################### task_1_var1 ####################


def parse_auto_number_1(auto_number):
    if not isinstance(auto_number, str):
        raise Exception('There should be a string')
    result_of_parsing = None
    template_list = [r'([A-Я]{2}[1-9]{4}[А-Я]{2})',
                     r'([0-9]{2}\s[0-9]{3}-[1-9]{2}[А-Я]{2})',
                     r'([а-я]{1}[0-9]{5}[А-Я]{2})']

    for _ in range(len(template_list)):
        if re.search(template_list[_], auto_number):
            result_of_parsing = auto_number
            break

    return result_of_parsing


def task_1_var1():
    print(parse_auto_number_1('а12345ВС'))  # valid
    print(parse_auto_number_1('12 123-45АВ'))  # valid
    print(parse_auto_number_1('АА1234ВВ'))  # valid
    print(parse_auto_number_1('АА1234__ВВ'))  # invalid
    print(parse_auto_number_1('Аa1234_ВВ'))  # invalid
    print(parse_auto_number_1('АA123!ВВ'))  # invalid
    print(parse_auto_number_1(123))  # invalid

# task_1_var1()

#################### task_1_var2 ####################


def parse_auto_number_2(auto_number):
    if not isinstance(auto_number, str):
        raise Exception('There should be a string')
    template = r'([A-Я]{2}|[0-9]{2}\s|[а-я]{1})([0-9]{2}|[0-9]{3}|[0-9]{3}-)[0-9]{2}[А-Я]{2}'
    result_of_search = re.search(template, auto_number)
    return auto_number if result_of_search else result_of_search


def task_1_var2():
    print(parse_auto_number_2('а12345ВС'))  # valid
    print(parse_auto_number_2('12 123-45АВ'))  # valid
    print(parse_auto_number_2('АА1234ВВ'))  # valid
    print(parse_auto_number_2('АА1234__ВВ'))  # invalid
    print(parse_auto_number_2('Аa1234_ВВ'))  # invalid
    print(parse_auto_number_2('АA123!ВВ'))  # invalid
    print(parse_auto_number_2(123))  # invalid

# task_1_var2()


#######################################################################################################


#################### task_2_var1 ####################
class AutoNumberFinderV1:
    _lst_of_templates = [r'([A-Я]{2}[1-9]{4}[А-Я]{2})',
                         r'([0-9]{2}\s[0-9]{3}-[1-9]{2}[А-Я]{2})',
                         r'([а-я]{1}[0-9]{5}[А-Я]{2})']
    _target_text = ''

    def __init__(self, lst_of_templates=[], target_text=''):
        self._lst_of_templates = lst_of_templates
        self._target_text = target_text

    @property
    def lst_of_templates(self):
        return self._lst_of_templates

    @lst_of_templates.setter
    def lst_of_templates(self, lst_of_templates):
        if not isinstance(lst_of_templates, list):
            raise Exception('It should be LIST of templates')
        for _ in range(len(lst_of_templates)):
            if isinstance(lst_of_templates[_], str):
                self._lst_of_templates = lst_of_templates
            else:
                raise Exception('Check list elements, they should be STRing')

    @property
    def target_text(self):
        return self._target_text

    @target_text.setter
    def target_text(self, target_text):
        if not isinstance(target_text, str):
            raise Exception('Object for parsing should be STRing.')
        self._target_text = target_text

    def find_auto_numbers(self):
        counter = 0
        # print(self._lst_of_templates)
        for pattern in self._lst_of_templates:
            # print(pattern)
            for number in re.findall(pattern, self._target_text):
                counter += 1
                print(counter, number)


def task_2_v1():

    a_n_f = AutoNumberFinderV1()
    print(a_n_f.lst_of_templates)
    print(a_n_f.target_text)
    print('*'*100)

    list_of_tmpl = [r'([A-Я]{2}[1-9]{4}[А-Я]{2})',
                    r'([0-9]{2}\s[0-9]{3}-[1-9]{2}[А-Я]{2})',
                    r'([а-я]{1}[0-9]{5}[А-Я]{2})']
    a_n_f.lst_of_templates = list_of_tmpl

    text = '12 123-45АВКУвав ваыа12345ВСКУ99 999-99АА!"3_15щз63 551-75ЫЗАА1234ВВ'
    a_n_f.target_text = text

    print(a_n_f.lst_of_templates)
    print(a_n_f.target_text)
    print('*' * 100)

    print(a_n_f.find_auto_numbers())


# task_2_v1()


#################### task_2_var2 ####################
class AutoNumberFinderV2:
    _template = r''
    _target_text = ''
    _numbered_dct = {}

    def __init__(self, lst_of_templates=r'', target_text=''):
        self._lst_of_templates = lst_of_templates
        self._target_text = target_text

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        if not isinstance(template, str):
            raise Exception('It should be STRing of templates')
        if not template:
            raise Exception('There is not any text')
        else:
            self._template = template

    @property
    def target_text(self):
        return self._target_text

    @target_text.setter
    def target_text(self, target_text):
        if not isinstance(target_text, str):
            raise Exception('Object for parsing should be STRing.')
        if not target_text:
            raise Exception('There is not any text')
        self._target_text = target_text

    def find_auto_numbers(self):
        _result_of_parsing = re.findall(self._template, self._target_text)
        counter = 1
        for number in _result_of_parsing:
            self._numbered_dct.update({counter: number})
            counter += 1
        return self._numbered_dct


def task_2_v2():

    a_n_f_2 = AutoNumberFinderV2()
    print('right now template is: ', a_n_f_2.template)
    print('right now text is: ', a_n_f_2.target_text)
    print('*'*100)

    tmpl = r'([A-Я]{2}[1-9]{4}[А-Я]{2})'
    a_n_f_2.template = tmpl

    text = '12 123-45АВКУвав АА1234АВ ваыа12345ВСКУ АА1234БВ 99 999-99АА!"3_15щз63 551-75ЫЗ АА1234ВВ'
    a_n_f_2.target_text = text

    print('after changes template is: ', a_n_f_2.template)
    print('after changes template is: ', a_n_f_2.target_text)
    print('*' * 100)

    print(a_n_f_2.find_auto_numbers())


# task_2_v2()
