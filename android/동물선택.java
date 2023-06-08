package sch.sch1.sch2.survey;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;

import sch.sch1.sch2.survey.R;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onClicked(View view) {
        switch (view.getId()) {
            case R.id.button:
                RadioButton dog = findViewById(R.id.radio1);
                RadioButton cat = findViewById(R.id.radio2);
                RadioButton bird = findViewById(R.id.radio3);
                ImageView imageView = findViewById(R.id.imageView);

                if (dog.isChecked()) {
                    imageView.setImageResource(R.drawable.dog);
                } else if (cat.isChecked()) {
                    imageView.setImageResource(R.drawable.cat);
                } else if (bird.isChecked()) {
                    imageView.setImageResource(R.drawable.bird);
                }
                break;
        }
    }
}
