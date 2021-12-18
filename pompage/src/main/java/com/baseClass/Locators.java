package com.baseClass;

import org.openqa.selenium.By;

public class Locators {

	//Login page variable
	public By LP_email_name=By.name("em");
	public By LP_email_id=By.id("email");
	public By LP_email_css=By.cssSelector(".input-box:nth-child(1) > #email");
	public By LP_email_xpath=By.xpath("//input[@id=\'email\']");
	public By LP_password_name=By.name("pass");
	public By LP_password_id=By.id("password");
	public By LP_password_css=By.cssSelector(".input-box:nth-child(2) > #pass");
	public By LP_password_type=By.xpath("//input[@type=\"password\"]");
	public By LP_password_xpathid=By.xpath("//input[@id=\'pass\']");
	public By LP_loginbutton=By.cssSelector(".button:nth-child(4) > input");
	public By LP_signupbutton_css=By.cssSelector(".text:nth-child(5) > label");
	public By LP_signupbutton_xpath=By.xpath("//label[contains(.,\'Sigup now\')]");
	
	//Register page variable
	public By RP_image_css=By.cssSelector(".cover");
	public By RP_image_xpath=By.xpath("//div/div");
	public By RP_heading_css=By.cssSelector(".signup-form > .title");
	public By RP_heading_xpath=By.xpath("//div[2]/div/div[2]/div");
	public By RP_name_id=By.id("name");
	public By RP_name_name=By.name("name");
	public By RP_name_xpath=By.xpath("//input[@id=\\'name\\']");
	public By RP_name_css=By.cssSelector("#name");
	public By RP_uname_id=By.id("uname");
	public By RP_uname_name=By.name("uname");
	public By RP_uname_xpath=By.xpath("//input[@id=\\'uname\\']");
	public By RP_uname_css=By.cssSelector("#uname");
	public By RP_email_id=By.id("email1");
	public By RP_email_name=By.name("email1");
	public By RP_email_xpath=By.xpath("//input[@id=\'email1\']");
	public By RP_email_css=By.cssSelector("#email1");
	public By RP_number_id=By.id("num");
	public By RP_number_name=By.name("num");
	public By RP_number_xpath=By.xpath("//input[@id=\'num\']");
	public By RP_number_css=By.cssSelector("#num");
	public By RP_password_id=By.id("pass1");
	public By RP_password_name=By.name("pass1");
	public By RP_password_xpath=By.xpath("//input[@id=\'pass1\']");
	public By RP_password_css=By.cssSelector("#pass1");
	public By RP_password_type=By.xpath("//input[@type=\'password\']");
	public By RP_submitbutton_id=By.id("btn");
	public By RP_submitbutton_name=By.name("submit");
	public By RP_submitbutton_xpath=By.xpath("//input[@id=\'btn\']");
	public By RP_submitbutton_css=By.cssSelector("#btn");
	public By RP_loginpagebutton_xpath=By.xpath("//label[contains(.,\'Login now\')]");
	
	//Home page variable
	
	public By Home_heading_linkText=By.linkText("Crypto Currency");
	public By Home_heading_css=By.cssSelector(".navbar-brand");
	public By Home_heading_xpath1=By.xpath("//a[contains(text(),\'Crypto Currency\')]");
	public By Home_heading_xpath2=By.xpath("//a[contains(@href, \'Aboutcrpy.php\')]");
	public By Home_search_css=By.cssSelector(".navbar-nav > a:nth-child(1)");
	public By Home_search_xpath1=By.xpath("//a[contains(text(),\'Search\')]");
	public By Home_search_xpath2=By.xpath("//a[contains(@href, \'https://crypto-tracker.swapnilg4u.repl.co/\')]");
	public By Home_search_xpath3=By.xpath("//div/div/a");
	public By Home_developer_css=By.cssSelector(".navbar-nav > a:nth-child(2)");
	public By Home_developer_xpath1=By.xpath("//a[contains(text(),\'Developer\')]");
	public By Home_developer_xpath2=By.xpath("//a[contains(@href, \'creator.html\')]");
	public By Home_developer_xpath3=By.xpath("//a[2]");
	public By Home_logout_xpath1=By.xpath("//a[contains(text(),\'Logout\')]");
	public By Home_logout_xpath2=By.xpath("//a[contains(@href, \'index.html\')]");
	public By Home_logout_xpath3=By.xpath("//a[3]");
	public By Home_bgImageText_xpath1=By.xpath("//span[contains(.,\'Crypto Currency\')]");
	public By Home_bgImageText_xpath2=By.xpath("//span");
	public By Home_bgImageText_css=By.cssSelector("span:nth-child(1)");
	public By Home_bgImageDesc_css=By.cssSelector(".container > p");
	public By Home_bgImageDesc_xpath=By.xpath("//p");
	public By Home_bgImage_css=By.cssSelector(".banner");
	public By Home_bgImage_xpath=By.xpath("//header/div");
	public By Home_Image1_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div/div[2]/h2");
	public By Home_Image1_xpath2=By.xpath("//div[2]/h2");
	public By Home_Image1_xpath3=By.xpath("//h2[contains(.,\'ShibElon\')]");
	public By Home_Image1_css=By.cssSelector(".design-item:nth-child(1) h2");
	public By Home_Image2_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div[2]/div[2]/h2");
	public By Home_Image2_xpath2=By.xpath("//div[2]/div[2]/h2");
	public By Home_Image2_xpath3=By.xpath("//h2[contains(.,\'Bitcoine\')]");
	public By Home_Image2_css=By.cssSelector(".design-item:nth-child(2) h2");
	public By Home_Image3_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div[3]/div[2]/h2");
	public By Home_Image3_xpath2=By.xpath("//div[3]/div[2]/h2");
	public By Home_Image3_xpath3=By.xpath("//h2[contains(.,\'Ethereum\')]");
	public By Home_Image3_css=By.cssSelector(".design-item:nth-child(3) h2");
	public By Home_Image4_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div[4]/div[2]/h2");
	public By Home_Image4_xpath2=By.xpath("//div[4]/div[2]/h2");
	public By Home_Image4_xpath3=By.xpath("//h2[contains(.,\'DogeCoin\')]");
	public By Home_Image4_css=By.cssSelector(".design-item:nth-child(4) h2");
	public By Home_Image5_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div[5]/div[2]/h2");
	public By Home_Image5_xpath2=By.xpath("//div[5]/div[2]/h2");
	public By Home_Image5_xpath3=By.xpath("//h2[contains(.,\'Binance Coin\')]");
	public By Home_Image5_css=By.cssSelector(".design-item:nth-child(5) h2");
	public By Home_Image6_xpath1=By.xpath("//section[@id=\'design\']/div/div[2]/div[6]/div[2]/h2");
	public By Home_Image6_xpath2=By.xpath("//h2[contains(.,\'Ripple Coin\')]");
	public By Home_Image6_css=By.cssSelector(".design-item:nth-child(6) h2");
	public By Home_contentImg_css=By.cssSelector(".about-content img");
	public By Home_contentImg_xpath1=By.xpath("//section[@id=\'about\']/div/div/div/img");
	public By Home_contentImg_xpath2=By.xpath("//section[2]/div/div/div/img");
	public By Home_sociallink_css=By.cssSelector(".social-links");
	public By Home_sociallink_xpath=By.xpath("//footer/div");
	
	//Search Page
	public By SP_SearchBox_xpath=By.xpath("//input[@id='myInput']");
	public By SP_heading_xpath=By.xpath("//a[contains(text(),'Real Time Crypto Tracker')]");
	public By SP_heading_text=By.linkText("Real Time Crypto Tacker");
	public By SP_ADX_text=By.linkText("ADX");
	public By SP_ADX_xpath1=By.xpath("/a[contains(text(),'ADX')]");
	public By SP_ADX_xpath2=By.xpath("//ul[@id='myUL']/li[4]/a");

	//Developer page
	public By DP_Heding_xpath= By.xpath("//a[contains(text(),'Crypto Currency')]");
	public By DP_Search_xpath= By.xpath("//a[contains(text(),'Search')]");
	public By DP_Developer_xpath= By.xpath("//a[contains(text(),'Developer')]");
	public By DP_Logout_xpath= By.xpath("//a[contains(text(),'Logout')]");
	
	public By DP_Text2_xpath= By.xpath("//h2[contains(.,'Developers & Designers')]");//Developers and designers
	public By DP_Image= By.xpath("//section[@id='design']/div/div[2]/div/div/span");//Akash pic
	
	//Graph Page
	public By GP_footer_xpath =By.id("//div[@id='credit']");
	public By GP_footer_id =By.id("credit");
	public By GP_button_xpath =By.xpath("//button[@type='button']");
	
	
}
