package sch.sch1.sch2.myapplicationcc;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    View view1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        view1=findViewById(R.id.layout);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu){
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.mymenu, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        switch (item.getItemId()){
            case R.id.blue :
                view1.setBackgroundColor(Color.BLUE);
                return true;
            case R.id.green :
                view1.setBackgroundColor(Color.GREEN);
                return true;
            case R.id.red :
                view1.setBackgroundColor(Color.RED);
                return true;
            default:
        }
        return super.onOptionsItemSelected(item);
    }
}
