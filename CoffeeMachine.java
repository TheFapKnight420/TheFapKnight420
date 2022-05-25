
import java.util.Scanner;
public class CoffeeMachine {
    private static CoffeeMaker maker;
    private static Scanner scanner;

    public static void main(String[] args) {
        scanner = new Scanner(System.in);
        maker = new CoffeeMaker();

        // Get Action
        String action;
        do {
            System.out.println("\nWrite action (buy, fill, take, remaining, exit):");
            action = scanner.nextLine();
            action(action);
        } while (!action.equals("exit"));
    }

    private static void action(String action) {
        switch (action){
            case "buy":
                // If user want to buy a coffee
                orderCoffee();
                break;
            case "fill":
                // Ask the user to full the machine
                inputMaterials();
                break;
            case "take":
                System.out.printf("I gave you $%d\n", maker.takeMoney());
                break;
            case "remaining":
                System.out.println();
                maker.printState();
        }
    }

    public static void orderCoffee(){
        Coffee[] coffees = {
                new Coffee(250, 0, 16, 4),
                new Coffee(350, 75, 20, 7),
                new Coffee(200, 100, 12, 6),
        };

        System.out.println("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:");
        String coffeeInput = scanner.nextLine();
        if (coffeeInput.equals("back")){
            return;
        }
        int coffeeNumber = Integer.parseInt(coffeeInput);
        if (coffeeNumber <= 3 && coffeeNumber >= 1){
            maker.makeCoffee(coffees[coffeeNumber - 1]);
        }
    }

    private static void inputMaterials(){
        System.out.println();
        // Ask and input the ingredients in coffee machine
        System.out.println("Write how many ml of water you want to add:");
        int numWater = scanner.nextInt();
        System.out.println("Write how many ml of milk you want to add:");
        int numMilk = scanner.nextInt();
        System.out.println("Write how many grams of coffee beans you want to add:");
        int numCoffeeBeans = scanner.nextInt();
        System.out.println("Write how many disposable cups of coffee you want to add:");
        int numCups = scanner.nextInt();

        maker.water += numWater;
        maker.milk += numMilk;
        maker.coffeeBeans += numCoffeeBeans;
        maker.disposableCups += numCups;
    }
}

class CoffeeMaker {
    public int water = 400;
    public int milk = 540;
    public int coffeeBeans = 120;
    public int disposableCups = 9;
    public int currentMoney = 550;

    CoffeeMaker(){

    }

    public void makeCoffee(Coffee coffee){
        // Make the coffee
        if (water >= coffee.water && milk >= coffee.milk && coffeeBeans >= coffee.coffeeBeans && disposableCups >= 0){
            System.out.println("I have enough resources, making you a coffee!");
            water -= coffee.water;
            milk -= coffee.milk;
            coffeeBeans -= coffee.coffeeBeans;
            disposableCups--;
            currentMoney += coffee.cost;
        }
        else{
            // Not enough resources
            // Determine what is the problem
            if (water < coffee.water){
                System.out.println("Sorry, not enough water!");
            }
            if (milk < coffee.milk){
                System.out.println("Sorry, not enough milk!");
            }
            if (coffeeBeans < coffee.coffeeBeans){
                System.out.println("Sorry, not enough coffee beans!");
            }
            if (disposableCups < 1){
                System.out.println("Sorry, not enough cups!");
            }
        }
    }

    public void printState(){
        System.out.println("The coffee machine has:");
        System.out.printf("%d ml of water\n", water);
        System.out.printf("%d ml of milk\n", milk);
        System.out.printf("%d g of coffee beans\n", coffeeBeans);
        System.out.printf("%d disposable cups\n", disposableCups);
        System.out.printf("$%d of money\n", currentMoney);
    }

    public int takeMoney(){
        int money = currentMoney;
        currentMoney = 0;
        return money;
    }
}

class Coffee{
    public Coffee(int water, int milk, int coffeeBeans, int cost) {
        this.water = water;
        this.milk = milk;
        this.coffeeBeans = coffeeBeans;
        this.cost = cost;
    }

    public int water;
    public int milk;
    public int coffeeBeans;
    public int cost;
}