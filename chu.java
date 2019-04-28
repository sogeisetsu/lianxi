public class chu
{
	public static void main(String[] args){
		int x =1;
		int y =2 ;
		for (int a =1;a<=10 ;a++ )
		{
			for (int b =1;b<=a+1 ;b++ )
			{
				if (b==a)
				{
					continue;
				}
				System.out.println("b="+b);
				System.out.println("a="+a);
			}
		}

	}
}
