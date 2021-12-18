package com.TestCases;

import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.Pages.HomePage;
import com.Pages.LoginPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.BaseClass;
import com.baseClass.Helper;
import com.baseClass.Locators;
import com.baseClass.Utility;

public class HomePageTest {
	private static final String priority = null;
	HomePage HomePage;
	BaseClass BaseClass;
	LoginPage LoginPage;
	Locators Locators = new Locators();

	Utility utils = new Utility();
	WebDriver driver = utils.setup();

	static ExtentSparkReporter htmlReporter;

	static ExtentReports extent;

	static ExtentTest test1;

	@BeforeTest

	public void beforeMethod() {

		// BrowserSetup.setup("chrome");

		htmlReporter = new ExtentSparkReporter("HomePageReport.html");

		extent = new ExtentReports();

		extent.attachReporter(htmlReporter);

	}

	public void WebSetup() {
		driver.get("http://localhost/CryptoTracker/Aboutcrpy.html");
		HomePage = new HomePage(driver);

	}
	// SC_01_TC_01 is editable)

	@Test(priority = 1)

	public void MousHover() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforeHPmousehover1");

		test1 = extent.createTest("HomePage MousHover", "TestCase1");

		HomePage.mouseHoverOnElement(Locators.Home_heading_xpath1);

		test1.pass("Home heading mouse hover effect");
		HomePage.mouseHoverOnElement(Locators.Home_search_xpath1);

		test1.pass("Home Search button mouse hover effect");

		HomePage.mouseHoverOnElement(Locators.Home_developer_xpath1);

		test1.pass("Home Developer Button mouse hover effect");

		HomePage.mouseHoverOnElement(Locators.Home_logout_xpath1);

		test1.pass("Home Logout Button mouse hover effect");

		HomePage.mouseHoverOnElement(Locators.Home_Image1_xpath1);

		test1.pass("Home Image 1 mouse hover effect");

		HomePage.mouseHoverOnElement(Locators.Home_Image2_xpath2);

		test1.pass("Home image2 mouse hover effect");

		HomePage.mouseHoverOnElement(Locators.Home_sociallink_xpath);

		test1.pass("Home Social Media Tags mouse hover effect");

		Helper.captureScreenshot(driver, " AfterHPmousehover1");

	}

	@Test(priority = 2)// Button Asserted) 

	public void AssertText() throws Exception { 

		WebSetup(); 

		Helper.captureScreenshot(driver, "Before Heading Asserted-HOMEPAGE"); 

		test1 = extent.createTest("Homepage AssertText", "TestCase2"); 

		HomePage.AssertGetText(Locators.Home_heading_xpath1, "Crypto Currency"); 

		test1.pass(" Heading asserted Crypto Currency "); 

		HomePage.AssertGetText(Locators.Home_search_xpath1, "SEARCH"); 

		test1.pass(" Heading asserted SEARCH "); 

		HomePage.AssertGetText(Locators.Home_developer_xpath1, "DEVELOPER"); 

		test1.pass(" Heading asserted DEVELOPER "); 

		HomePage.AssertGetText(Locators.Home_logout_xpath1, "LOGOUT"); 

		test1.pass(" Heading asserted LOGOUT "); 

		Helper.captureScreenshot(driver, "After Heading Asserted-HOMEPAGE"); 

 
	}
	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}

}
