# Обработка речевых сигналов импульсными нейронными сетями
<a href="https://english.nsu.ru/"><img alt="NSU Logo" src="https://www.nsu.ru/upload/iblock/6e4/NSU_logo_English_Green.svg"></a>
<a href="https://www.nsu.ru/n/mathematics-mechanics-department/"><img width="100" alt="MMF NSU Logo" src="https://sun9-28.userapi.com/impg/jonZ8iNpeZvjklhKeNEiCs19g_29lmOQ1oxX7w/IJXl_DVihKY.jpg?size=1000x1000&quality=96&sign=cdd1d15212699e8fdeb5c67db4eb69e4&type=album"></a>

**Новосибирский государственный университет, Механико-математический факультет, Кафедра вычислительных систем**


## Аннотация

**Студент: Михайлапов Денис Иванович** 

**Научный руководитель: Тарков Михаил Сергеевич**

Выпускная квалификационная работа посвящена исследованию распознавания речевых сигналов импульсными нейронными сетями. Принципиальным отличием данных сетей от классических нейронных сетей, является кодирование информации в виде интервалов между импульсами. Данных подход обеспечивает более высокую энергоэффективность и надёжность данной нейронной сети при аппаратной реализации.

В работе было проведено моделирование свёрточной импульсной нейронной сети с использованием языка программирования Pуthon и новой библиотеки машинного обучения Norse, исследована точность распознавания речевых сигналов на пяти различных наборах данных. Также было проведено квантование весов нейронной сети и исследована зависимость качества работы сети в зависимости от уровня квантования.

В работе приведены графики и таблицы. Исходный код с проведёнными экспериментами выложен на Github.


## Краткое описание работы

В качестве языка программирования используется язык `Python`. Мы заранее перевели аудиозаписи всех наборов данных в спектрограммы с помощью библиотеки `matplotlib` и сохранили их в виде отдельных папок с изображениями. Затем эти спектрограммы, посредством функционала `Norse`, переводятся в двумерные импульсные последовательности и подаются на вход сети (см. код класса `SCNN`). В конце мы оцениваем работу сети. Также мы исследуем поведение точности модели при квантовании весовых коэффициентов. Исходный код метода квантования можно найти во всех ноутбуках, а также отдельно в файле [Quant.py](https://github.com/DenisMihailapov/Norse-ASR/blob/main/Utils/Quant.py) из папки Utils. **Заметим**, что данный метод отличается от метода квантования модели приведённом в [torch.quantization](https://pytorch.org/docs/stable/torch.quantization.html?highlight=torch%20quantization#module-torch.quantization). 

## Описание репозитория
В данном репозиторий находятся численные эксперименты применения функционала библиотеки моделирования импульсных нейронных сетей [Norse](https://github.com/norse/norse), написанный на основе библиотеки глубокого машинного обучения [PyTorch](https://pytorch.org), для задачи распознавания речи.  

В папке [Notebook](https://github.com/DenisMihailapov/Norse-ASR/tree/main/Notebook) собраны все ноутбуки с чиленными экспериментами. Каждый ноутбук подписан в соответствии с распознаваемым набором данных.

В папке [Utils](https://github.com/DenisMihailapov/Norse-ASR/tree/main/Utils) собран исходный код утилит, написанных в ходе работы: 
 * [AudioLoader.py](https://github.com/DenisMihailapov/Norse-ASR/blob/main/Utils/AudioLoader.py) -- утилита для работы с аудиофайлами.
 * [SpikeUtils.py](https://github.com/DenisMihailapov/Norse-ASR/blob/main/Utils/SpikeUtils.py) -- утилита для работы со спайковыми последовотельностями (почти не использовалась).
 * [Quant.py](https://github.com/DenisMihailapov/Norse-ASR/blob/main/Utils/Quant.py) -- код метода квантования весов модели.


## Данные на Google drive
По следующим ссылкам можно получить доступ ко всем сохранённым моделям <a href="https://drive.google.com/drive/folders/1l4v2hvVaBlslLg54dugCF6AvMJnkvsm_?usp=sharing"><img width="32" alt="Google Drive with all image data" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Logo_of_Google_Drive_%282012-2014%29.svg/32px-Logo_of_Google_Drive_%282012-2014%29.svg.png"></a> и к папкам со спектрограммами <a href="https://drive.google.com/drive/folders/1WXKYQeFa2wTinAZ_7Pkv4LB3GJIbF_X9?usp=sharing"><img width="32" alt="Google Drive with all image data" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Logo_of_Google_Drive_%282012-2014%29.svg/32px-Logo_of_Google_Drive_%282012-2014%29.svg.png"></a>


## Текст работы
На данный момент мы не можем дать ссылку на текст работы.
_________________
2021г
