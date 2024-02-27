class Person {
    protected String name;
    protected String address;
    protected String phoneNumber;
    protected String email;

    Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String toString() {
        return "Person: " + name;
    }
}

class Employee extends Person {
    protected String office;
    protected int salary;
    protected String dateHired;

    Employee(String name, String office, int salary, String dateHired) {
        super(name);
        this.office = office;
        this.salary = salary;
        this.dateHired = dateHired;
    }

    public String toString() {
        return "Employee: " + name;
    }
}

class Faculty extends Employee {
    public static int LECTURER = 1;
    public static int ASSISTANT_PROFESSOR = 2;
    public static int ASSOCIATE_PROFESSOR = 3;
    public static int PROFESSOR = 4;

    protected String officeHours;
    protected int rank;

    Faculty(String name, String office, int salary, String dateHired, String officeHours, int rank) {
        super(name, office, salary, dateHired);
        this.officeHours = officeHours;
        this.rank = rank;
    }

    public String toString() {
        return "Faculty: " + name;
    }
}

class Staff extends Employee {
    protected String title;

    Staff(String name, String title) {
        super(name, "", 0, null);
        this.title = title;
    }

    public String toString() {
        return "Staff: " + getName();
    }
}

class Student extends Person {
    public static int FRESHMAN = 1;
    public static int SOPHOMORE = 2;
    public static int JUNIOR = 3;
    public static int SENIOR = 4;
    @SuppressWarnings("unused")
    private int classStatus;

    Student(String name, int classStatus) {
        super(name);
        this.classStatus = classStatus;
    }

    public String toString() {
        return "Student: " + name;
    }
}

