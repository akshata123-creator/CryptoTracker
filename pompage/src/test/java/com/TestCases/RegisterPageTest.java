package com.TestCases;

import org.apache.hc.client5.http.entity.mime.Header;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.Pages.HomePage;
import com.Pages.LoginPage;
import com.Pages.RegisterPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.BaseClass;
import com.baseClass.Locators;
import com.baseClass.Utility;
import com.baseClass.Helper;

public class RegisterPageTest extends Utility {
	private static final String priority = null;

	HomePage homePage;

	BaseClass BaseClass;
	RegisterPage RegisterPage;

	Utility utils = new Utility();
	WebDriver driver = utils.setup();
	Locators Locators = new Locators();

	Helper Helper = new Helper();

	static ExtentSparkReporter htmlReporter;

	static ExtentReports extent;

	static ExtentTest test1;

	@BeforeTest

	public void beforeMethod() {

		// BrowserSetup.setup("chrome");

		htmlReporter = new ExtentSparkReporter("RegisterPageReport.html");

		extent = new ExtentReports();

		extent.attachReporter(htmlReporter);

	}

	public void WebSetup() {
		driver.get("http://localhost/CryptoTracker/index.html");
		RegisterPage = new RegisterPage(driver);

	}

	// SC_01_TC_01 signup from login page and element present, editable,click

	// button)

	@Test(priority = 1)

	public void EditableLogin() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforeRPeditable");

		test1 = extent.createTest("EditableLogin beffore register", "TestCase1");

		RegisterPage.elementPresent(Locators.LP_email_id);
		test1.pass("email id is present");

		RegisterPage.fieldEditable(Locators.LP_email_id);

		test1.pass("email id is editable");

		Helper.captureScreenshot(driver, "AfterRPPeditableT1");

	}

	// SC_01_TC_02 (element present, editable)

	@Test(priority = 2)

	public void RegisterElementPresent() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforeRPelementpresent");

		test1 = extent.createTest("RegisterPage ElementPresent", "TestCase2");

		RegisterPage.ClickButton(Locators.LP_signupbutton_xpath);

		test1.pass("Switch to Register Page");

		Helper.captureScreenshot(driver, "MidRPelementpresentT2");

		RegisterPage.elementPresent(Locators.RP_heading_xpath);

		test1.pass("Heading is Present");

		RegisterPage.elementPresent(Locators.RP_name_id);

		test1.pass(" name is Present ");

		RegisterPage.elementPresent(Locators.RP_uname_id);

		test1.pass(" Username is Present ");

		RegisterPage.elementPresent(Locators.RP_email_id);

		test1.pass(" Email is Present ");

		RegisterPage.elementPresent(Locators.RP_number_xpath);

		test1.pass(" Number is Present ");
		RegisterPage.elementPresent(Locators.RP_password_id);

		test1.pass(" Password is Present ");

		RegisterPage.elementPresent(Locators.RP_submitbutton_id);

		test1.pass(" Submit Button is Present ");

		RegisterPage.elementPresent(Locators.RP_loginpagebutton_xpath);

		test1.pass("Switch to Register Page Button");

		Helper.captureScreenshot(driver, "AfterRPelementpresentT2");

	}

	// SC_01_TC_03 (element present, editable)

	@Test(priority = 3)

	public void Editable() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "Before RegisterEditable");

		test1 = extent.createTest("RegisterPage Editable", "TestCase3");

		RegisterPage.ClickButton(Locators.LP_signupbutton_xpath);

		test1.pass("Signup Button is present");

		test1.pass("Switch to Register Page");

		Helper.captureScreenshot(driver, "Mid_RP_elementpresentT3");

		RegisterPage.fieldEditable(Locators.RP_name_id);

		test1.pass(" name id is editable ");

		RegisterPage.fieldEditable(Locators.RP_uname_id);

		test1.pass(" username id is editable ");

		RegisterPage.fieldEditable(Locators.RP_email_id);

		test1.pass(" email id is editable ");

		RegisterPage.fieldEditable(Locators.RP_number_xpath);

		test1.pass(" number id is editable ");

		RegisterPage.fieldEditable(Locators.RP_password_id);

		test1.pass("password id is editable ");

		RegisterPage.fieldEditable(Locators.RP_submitbutton_id);

		test1.pass(" Submit Button is editable ");

		Helper.captureScreenshot(driver, "After RegisterEditable");

	}

	// SC_01_TC_04 (Registration done successfully)

	@Test(priority = 4)

	public void registerTest() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "Before Registration done");

		test1 = extent.createTest("RegisterPage New account created successfully", "TestCase4");

		RegisterPage.ClickButton(Locators.LP_signupbutton_xpath);

		test1.pass("Signup Button is present");

		Thread.sleep(2000);

		RegisterPage.fun_register("aaakash", "assshhh", "aaakash@gmail.com", "9876543210", "Aaakash@123");

		test1.pass(" Registration done ");

		Helper.captureScreenshot(driver, "After Registration");

		//System.out.println("pass");

		Thread.sleep(2000);

		// driver.close();

	}

	// SC_01_TC_05(Account Already Exist)

	@Test(priority = 5)

	public void sameUsername() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "Before Registration TC5");

		test1 = extent.createTest("RegisterPage Account Already Exist", "TestCase5");

		RegisterPage.ClickButton(Locators.LP_signupbutton_xpath);

		test1.pass("Signup Button is clickable");

		Thread.sleep(2000);

		RegisterPage.fun_register("aaakash", "kashh", "aaakash@gmail.com", "9876543210", "Aaakash@123");

		test1.fail("Usename allready exist");

		Helper.captureScreenshot(driver, "After Registration");

		//System.out.println("pass");

		Thread.sleep(2000);

	}

	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}

}
