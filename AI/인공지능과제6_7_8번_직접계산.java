package java7장_과제;

import java.util.*;

public class ArrayListEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		double w5 = ((12 - 28.4) * (2015 - 2017) + (19 - 28.4) * (2016 - 2017) + (28 - 28.4) * (2017 - 2017) + (37 - 28.4) * (2018 - 2017) + (46 - 28.4) * (2019 - 2017)) / 
				((2015 - 2017) * (2015 - 2017) + (2016 - 2017) * (2016 - 2017) + (2017 - 2017) * (2017 - 2017) + (2018 - 2017) * (2018 - 2017) + (2019 - 2017) * (2019 - 2017));

		System.out.println(w5);
		
		double b5=28.4-w5*2017;
		System.out.println(b5);
		
		double result=w5*2020+b5;
		System.out.println(result);
		System.out.println();

		double x6=(1930+1940+1950+1965+1972+1982+1992+2010+2016)/9;
		double y6=(59+62+70+69+71+74+75+76+78)/9;
		System.out.println(x6+","+y6);
		double w6 = ((1930-x6)*(59-y6)+(1940-x6)*(62-y6)+(1950-x6)*(70-y6)+(1965-x6)*(69-y6)+(1972-x6)*(71-y6)+(1982-x6)*(74-y6)+(1992-x6)*(75-y6)+(2010-x6)*(76-y6)+(2016-x6)*(78-y6))
				/((1930-x6)*(1930-x6)+(1940-x6)*(1940-x6)+(1950-x6)*(1950-x6)+(1965-x6)*(1965-x6)+(1972-x6)*(1972-x6)+(1982-x6)*(1982-x6)+(1992-x6)*(1992-x6)+(2010-x6)*(2010-x6)+(2016-x6)*(2016-x6));

		System.out.println(w6);
		
		double b6=y6-w6*x6;
		System.out.println(b6);
		
		
		double result6=w6*1962+b6;
		System.out.println(result6);
		
		
		System.out.println();
		float x7=(float)(30+35+20+15+3)/(float)5;
		float y7=(float)(90+95+70+40+10)/(float)5;
		System.out.println(x7+","+y7);
		float w7 = (float)((float)(30-(float)x7)*(float)(90-(float)y7)+(float)(35-(float)x7)*(float)(95-(float)y7)+(float)(20-(float)x7)*(float)(70-(float)y7)+(float)(15-(float)x7)*(float)(40-(float)y7)+(float)(3-(float)x7)*(float)(10-(float)y7))
				/(float)((float)(30-(float)x7)*(float)(30-(float)x7)+(float)(35-(float)x7)*(float)(35-(float)x7)+(float)(20-(float)x7)*(float)(20-(float)x7)+(float)(15-(float)x7)*(float)(15-(float)x7)+(float)(3-(float)x7)*(float)(3-(float)x7));

		System.out.println(w7);
		
		float b7=(float)y7-w7*x7;
		System.out.println(b7);
		
		
	
	}
}
