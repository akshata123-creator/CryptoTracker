package com.TestCases;

import org.testng.Assert;
import org.testng.ITestResult;

import java.io.IOException;
import java.util.HashMap;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
//import org.xml.sax.Locator;
import com.baseClass.Locators;
import com.Pages.HomePage;
import com.Pages.LoginPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.Utility;
import com.baseClass.Helper;
//import com.baseClass.BaseClass;

public class LoginPageTest extends Utility {
	private static final String priority = null;
	HomePage homePage;
	// BaseClass BaseClass;
	LoginPage LoginPage;
	Locators Locators = new Locators();

	Utility utils = new Utility();
	WebDriver driver = utils.setup();
	Helper Helper = new Helper();

	static ExtentSparkReporter htmlReporter;
	static ExtentReports extent;
	static ExtentTest test1;

	@BeforeTest
	public void beforeMethod() {

		// BrowserSetup.setup("chrome");
		htmlReporter = new ExtentSparkReporter("LoginPageReport.html");
		extent = new ExtentReports();
		extent.attachReporter(htmlReporter);
	}

	public void WebSetup() {
		driver.get("http://localhost/CryptoTracker/index.html");
		LoginPage = new LoginPage(driver);

	}

	// SC_01_TC_01 is editable)
	@Test(priority = 1)
	public void Editable() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforLoginEditable");
		test1 = extent.createTest("LoginPage Editable", "TestCase1");
		LoginPage.fieldEditable(Locators.LP_email_id);
		test1.pass("email id is editable");
		LoginPage.fieldEditable(Locators.LP_password_xpathid);
		test1.pass("Password id is editable");
		LoginPage.fieldEditable(Locators.LP_loginbutton);
		test1.pass("Login button id is editable");
		LoginPage.fieldEditable(Locators.LP_signupbutton_xpath);
		test1.pass("signup id is editable");

		Helper.captureScreenshot(driver, "AfterLoginEditable");
	}

	// SC_01_TC_02 Mous Hover effect )

	@Test(priority = 2)
	public void MouseHover() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforLoginMouseHover");
		test1 = extent.createTest("LoginPage MouseHover", "TestCase2");
		LoginPage.mouseHoverOnElement(Locators.LP_email_id);
		test1.pass("Mouse Hover on email id");
		LoginPage.mouseHoverOnElement(Locators.LP_password_xpathid);
		test1.pass("Mouse Hover on Password");
		LoginPage.mouseHoverOnElement(Locators.LP_loginbutton);
		test1.pass("Mouse Hover on LoginButton");
		LoginPage.mouseHoverOnElement(Locators.LP_signupbutton_xpath);
		test1.pass("Mouse Hover on SignUp");
		Helper.captureScreenshot(driver, "AfterLoginMouseHover");
		

	}

	// SC_01_TC_03 (Valid Email and Password)

	@Test(priority = 3)
	public void loginTest() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforLoginloginTest");
		test1 = extent.createTest("LoginPage Valid Email and Password", "TestCase3");
		LoginPage.fun_login("rohini@gmail.com", "Rohini@123");
		test1.pass("Login details");
		Helper.captureScreenshot(driver, "AfterLoginloginTest");
		
	}

	// SC_01_TC_04 (Valid Email and incorrect Password)

	@Test(priority = 4)
	public void CheckPassword() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforLoginCheckPassword");
		test1 = extent.createTest("LoginPage Valid Email and incorrect Password", "TestCase4");
		LoginPage.fun_login("rohini@gmail.com", "Rohini@12"); 
		test1.pass("Invalid Login details");
		//System.out.println("pass");
		Helper.captureScreenshot(driver, "AfterLoginCheckPassword");
	}

	// SC_01_TC_05 Login Sccessfull and open Homepage)

	@Test(priority = 5)
	public void OpenHomePage() throws Exception {
		WebSetup();
		test1 = extent.createTest("OpenHomePage open Successfully", "TestCase5");
		LoginPage.fun_login("rohini@gmail.com", "Rohini@123");
		test1.pass("Login Sccessfull and open Homepage");
		Helper.captureScreenshot(driver, "AfterLoginOpenHomePage");
				

	}

	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}
	

}
