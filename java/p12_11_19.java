// Compile with:
// javac p12_11_19.java && java p12_11_19 foo bar baz

public class p12_11_19
{
	public static void main(String[] args)
	{
		System.out.println("Hello World!");

		for (String arg : args)
		{
			System.out.println(arg);

			for (int i = 0; i < arg.length(); i++)
			{
				System.out.println(arg.charAt(i));
			}
		}
	}	
}
