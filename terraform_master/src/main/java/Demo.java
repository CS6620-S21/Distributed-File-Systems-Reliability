//import jdk.nashorn.internal.parser.JSONParser;
//import org.json.JSONObject;
//import org.json.JSONTokener;

import java.io.*;


public class Demo {


    private static void  getJsonObject(Process p) {
//        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
//        JSONTokener tokener = new JSONTokener(stdInput);
//        JSONObject json = new JSONObject(tokener);
//        System.out.println(json.toString());
    }

    private static void logger(Process p) {
        String s = null;
        try {

            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));

            // read the output from the command
            System.out.println("Here is the standard output of the command:\n");
            while ((s = stdInput.readLine()) != null) {
                System.out.println(s);
            }

            // read any errors from the attempted command
            System.out.println("Here is the standard error of the command (if any):\n");
            while ((s = stdError.readLine()) != null) {
                System.out.println(s);
            }
            System.exit(0);
        }
        catch (IOException e) {
            System.out.println("exception happened - here's what I know: ");
            e.printStackTrace();
            System.exit(-1);
        }
    }

    private static void initializeTerraform() {
        String s = null;
        try {
            Process p = Runtime.getRuntime().exec("terraform init");
            logger(p);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void destroyTerraform() {
        String s = null;
        try {
            Process p = Runtime.getRuntime().exec("terraform destroy");
            logger(p);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void getOutput()  {

        Process p = null;
        try {
            p = Runtime.getRuntime().exec("terraform output -json");
            logger(p);
            getJsonObject(p);
        }
        catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static void executePlan() {

        try {
            Process p = Runtime.getRuntime().exec("sh terraform.runner.sh");
            logger(p);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static void main(String[] args) {
//        initializeTerraform();
//        executePlan();
        getOutput();
//        destroyTerraform();
    }
}
