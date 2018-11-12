package de.fuchs.playground.hashmap;

import java.util.HashMap;

public class MyHashMap {

    public static void main(String[] args) {

        HashMap hash1 = new HashMap();

        MyObject obj1 = new MyObject("Test1");
        MyObject obj2 = new MyObject("Test2");

        MyKey key1 = new MyKey();
        MyKey key2 = new MyKey();

        hash1.put(key1, obj1);
        hash1.put(key2, obj2);

        System.out.println("Hash map with conflict resolution... 2 non-equal objects with same hash (key objects are equal)");

        System.out.println(hash1);
        System.out.println(((MyObject)hash1.get(key1)).name);
        System.out.println(((MyObject)hash1.get(key2)).name);

        HashMap hash2 = new HashMap();

        MyKeyReplace keyConf1 = new MyKeyReplace();
        MyKeyReplace keyConf2 = new MyKeyReplace();

        hash2.put(keyConf1, obj1);
        hash2.put(keyConf2, obj2);

        System.out.println(" ");
        System.out.println("Hash map with no conflict resolution... 2 non-equal objects with same hash (but key objects are different)");

        System.out.println(hash2);
        System.out.println(((MyObject)hash2.get(keyConf1)).name);
        System.out.println(((MyObject)hash2.get(keyConf2)).name);

    }

}
