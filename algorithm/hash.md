## python dict/set 的实现

    hashtable 哈希表
    
* 哈希表的实现原理，底层是一个数组
* 根据哈希函数快速定位元素，查找 O(1)，非常快
* 不断加入元素会导致哈希表重新开辟空间，拷贝之前元素到新数组
* 如何解决 哈希冲突
    * 链接法
    * 开放寻址法（二次探查）x^2+y