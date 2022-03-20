package de.fuchs.playground.hashmap;

public class MyObject {

    public String name;

    public MyObject(String name) {
        this.name = name;
    }

    public boolean equals(Object o) {
        return name.equals(o);
    }

    public int hashCode() {
        return 1;
    }
}
