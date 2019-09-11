import java.io.*;
import java.util.*;
import java.util.Map.Entry;

class Bank
{
	private String name="";
	private int acc_no=0;
	private double balance=0.0;
	
	public Bank(String name, int acc_no, double balance)
	{
		this.name= name;
		this.acc_no= acc_no;
		this.balance=  balance;
	}
	
	public void withdrawal(double amt)
	{
		this.balance-= amt;
	}
	
	public void deposit(double amt)
	{
		this.balance+= amt;
	}
	
	public void checkBalance()
	{
		System.out.println("Current status of your account is:");
		System.out.println("User's name: "+this.name);
		System.out.println("Account No: "+this.acc_no);
		System.out.println("Balance : "+this.balance);
	}
	
	public String pass_gen()
	{
		final int len=3;
		Random rn= new Random();
		String password="";
		final String cap_char= "ABCDEFGHIJKLMNPQRSTUVWXYZ";
		final String small_char= "abcdefghijklmnpqstuvwxyz";
		final String digits= "123456789";
		final String letters= cap_char+small_char+digits;
		for(int i=0;i<len;i++)
		{
			password+= letters.charAt(rn.nextInt(letters.length()));
		}
		return password;
	}
	
	public int isValidAcc(int acc_no)
	{
		if(this.acc_no==acc_no)
			return 1;
		else
			return 0;
	}
	
	public double isEmpty()
	{
		return this.balance;
	}
	
	public int isAllowed(double amt)
	{
		if(amt>this.balance)
			return 0;
		else
			return 1;
	}
	
}

public class Banking_System
{
	public int isUsed(Map<Bank, String> user, int acc_no)
	{
		for(Entry<Bank, String> entry : user.entrySet())
		{
			if(entry.getKey().isValidAcc(acc_no)==1)
				return 1;
		}
		return 0;
	}

	public static void main(String[] args) throws IOException 
	{
		String name;
		int acc_no;
		double balance;
		String password;
		double amt;
		Bank key = null;
		Banking_System  bs= new Banking_System();
		InputStreamReader is= new InputStreamReader(System.in);
		BufferedReader br= new BufferedReader(is);
		Map<Bank, String> users= new HashMap<>();
		int f=1;
		
		while(f==1)
		{
			int ch;
			System.out.println("\n1.Create account\n2.Already have an account\n3.Exit");
			ch= Integer.parseInt(br.readLine());
			switch(ch)
			{
			case 1: System.out.println("Enter your name: ");
					name= br.readLine();
					System.out.println("Enter your account no: ");
					acc_no= Integer.parseInt(br.readLine());
					if(bs.isUsed(users, acc_no)==1)
					{
						System.out.println("Sorry, this account number has already been used");
						break;
					}
					else
					{
						System.out.println("Enter your starting balance: ");
						balance= Double.parseDouble(br.readLine());
						Bank usr= new Bank(name, acc_no, balance);
						password= usr.pass_gen();
						users.put(usr, password);
						System.out.println("Account has been created successfully");
						System.out.println("Your password is: "+password);
						System.out.println("Don't forget this password. If you forget you will lose control of your account");
						break;	
					}
					
			case 2: int flag=0;
					System.out.println("Enter your account no: ");
					acc_no= Integer.parseInt(br.readLine());
					System.out.println("Enter your password: ");
					password= br.readLine();
					for(Entry<Bank, String> entry : users.entrySet())
					{
						if(entry.getKey().isValidAcc(acc_no)==1 && entry.getValue().equals(password)==true)
						{
							key= entry.getKey();
							flag=1;
							break;
						}
					}
					if(flag==0)
						System.out.println("Sorry, account not found");
					else
					{
						int t=1;
						while(t==1)
						{
							int c;
							System.out.println("\n1.Withdrawal\n2.Deposit\n3.Check Balace\n4.Change password\n5.Delete Account\n6.Exit");
							c= Integer.parseInt(br.readLine());
							switch(c)
							{
							case 1: System.out.println("Enter the amount you want to withdrawal: ");
									amt= Double.parseDouble(br.readLine());
									if(key.isAllowed(amt)==1)
									{
										key.withdrawal(amt);
										key.checkBalance();
										t=0;
										break;
									}
									else
									{
										System.out.println("Sorry, not allowed");
										break;	
									}
									
							case 2: System.out.println("Enter the amount you want to deposit: ");
									amt= Double.parseDouble(br.readLine());
									key.deposit(amt);
									key.checkBalance();
									t=0;
									break;
									
							case 3: key.checkBalance();
									t=0;
									break;
									
							case 4: String passcode="";
									System.out.println("Enter the password you want: ");
									password= br.readLine();
									System.out.println("Confirm your password: ");
									passcode= br.readLine();
									if(password.contentEquals(passcode))
									{
										users.replace(key, password);
										System.out.println("Password has been changed successfully");
										t=0;
									}
									else
										System.out.println("Failed");
									break;
									
							case 5: String cnfm="";
									System.out.println("Are your sure about your decision? yes/no ");
									cnfm=br.readLine();
									if(cnfm.contentEquals("yes"))
									{
										if(key.isEmpty()==0.0)
										{
											users.remove(key);
											System.out.println("Account has been deleted successfully");
											t=0;
										}
										
										else
										{
											System.out.println("Please, collect all of your money beforr deleting your account.");
											break;
										}
									}
									else
										t=0;
									break;
									
							case 6: t=0;
									break;
							}
						}
					}
					break;
					
			case 3: System.out.println("Thank you....visit again....");
					f=0;
					
			default: break;
			}
		}
	}
}
