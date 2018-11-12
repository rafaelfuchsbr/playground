This code is to illustrate the key conflicts of Java's HashMap.

I like this explanation I found in stack overflow.

When you insert the pair (10, 17) and then (10, 20), there is technically no collision involved. You are just replacing the old value with the new value for a given key 10 (since in both cases, 10 is equal to 10 and also the hash code for 10 is always 10).

Collision happens when multiple keys hash to the same bucket. In that case, you need to make sure that you can distinguish between those keys. Chaining collision resolution is one of those techniques which is used for this.

As an example, let's suppose that two strings "abra ka dabra" and "wave my wand" yield hash codes 100 and 200 respectively. Assuming the total array size is 10, both of them end up in the same bucket (100 % 10 and 200 % 10). Chaining ensures that whenever you do map.get( "abra ka dabra" );, you end up with the correct value associated with the key. In the case of hash map in Java, this is done by using the equals method.

https://stackoverflow.com/questions/19691920/collision-resolution-in-java-hashmap/19691998