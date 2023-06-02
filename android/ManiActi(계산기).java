package sch.sch1.sch2.myapplicationcc;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private TextView text;
    private double storedValue;
    private char curOperator;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("정인호 계산기");

        text = findViewById(R.id.text);
    }

    public void onClick(View view) {
        String current = text.getText().toString();

        switch (view.getId()) {
            case R.id.n0:
                text.setText(current + "0");
                break;
            case R.id.n1:
                text.setText(current + "1");
                break;
            case R.id.n2:
                text.setText(current + "2");
                break;
            case R.id.n3:
                text.setText(current + "3");
                break;
            case R.id.n4:
                text.setText(current + "4");
                break;
            case R.id.n5:
                text.setText(current + "5");
                break;
            case R.id.n6:
                text.setText(current + "6");
                break;
            case R.id.n7:
                text.setText(current + "7");
                break;
            case R.id.n8:
                text.setText(current + "8");
                break;
            case R.id.n9:
                text.setText(current + "9");
                break;
            case R.id.ndot:
                text.setText(current + ".");
                break;
            case R.id.plus:
                if (current.equals("")) {
                    Toast.makeText(getApplicationContext(), "숫자를 먼저 입력하세요", Toast.LENGTH_SHORT).show();
                } else {
                    storedValue = Double.parseDouble(current);
                    curOperator = '+';
                    text.setText("");
                    break;
                }
            case R.id.sub:
                if (current.equals("")) {
                    Toast.makeText(getApplicationContext(), "숫자를 먼저 입력하세요", Toast.LENGTH_SHORT).show();
                } else {
                    storedValue = Double.parseDouble(current);
                    curOperator = '-';
                    text.setText("");
                    break;
                }
            case R.id.mul:
                if (current.equals("")) {
                    Toast.makeText(getApplicationContext(), "숫자를 먼저 입력하세요", Toast.LENGTH_SHORT).show();
                } else {
                    storedValue = Double.parseDouble(current);
                    curOperator = '*';
                    text.setText("");
                    break;
                }
            case R.id.div:
                if (current.equals("")) {
                    Toast.makeText(getApplicationContext(), "숫자를 먼저 입력하세요", Toast.LENGTH_SHORT).show();
                } else {
                    storedValue = Double.parseDouble(current);
                    curOperator = '/';
                    text.setText("");
                    break;
                }

            case R.id.clear:
                text.setText("");
                storedValue = 0.0;
                break;

            case R.id.Ok:
                if (current.equals("")) {
                    Toast.makeText(getApplicationContext(), "숫자를 먼저 입력하세요", Toast.LENGTH_SHORT).show();
                } else {
                    double result = 0;
                    double thisValue = Double.parseDouble(text.getText().toString());
                    switch (curOperator) {
                        case '+':
                            result = storedValue + thisValue;
                            break;
                        case '-':
                            result = storedValue - thisValue;
                            break;
                        case '*':
                            result = storedValue * thisValue;
                            break;
                        case '/':
                            result = storedValue / thisValue;
                            break;
                    }
                    text.setText("" + result);
                    storedValue = 0.0;
                    break;
                }
        }
    }
}
