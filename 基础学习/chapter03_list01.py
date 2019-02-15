## 第三章 列表简介 --20190127
#列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。
#要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
motorcycles = [' honda ','yamaha ','suzuki','ducati'];
print(motorcycles );
#索引从 0 而不是 1 开始
print(motorcycles[0] + "====");
# strip rstrip lrstrip 去空格
print(motorcycles[0].strip());

motorcycles.insert(1,'jianshe');
print(motorcycles );

# 删除指定索引的元素
del motorcycles[0];
print(motorcycles );
# pop() 取最后一个元素，也可以指定索引pop(1);
pop_motorcycles = motorcycles.pop();
print(motorcycles );
print(pop_motorcycles );

# renove 删除指定的元素；
motorcycles.remove('suzuki');
print(motorcycles );
# sort()，对列表永久排序；sorted()临时排序，一般用于打印；
motorcycles.sort();
print(motorcycles );
#确定列表的长度，索引越界将导致报错