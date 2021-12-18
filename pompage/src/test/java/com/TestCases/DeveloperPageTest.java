package com.TestCases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

//import com.Pages.Developer;
import com.Pages.DeveloperPage;
import com.Pages.HomePage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.BaseClass;
import com.baseClass.Helper;
import com.baseClass.Utility;
import com.baseClass.Locators;

public class DeveloperPageTest {
	BaseClass BaseClass;
	DeveloperPage DeveloperPage;
	Locators Locators = new Locators();
	static ExtentSparkReporter htmlReporter;
	static ExtentReports extent;
	static ExtentTest test1;

	Utility utils = new Utility();
	WebDriver driver = utils.setup();

	@BeforeTest
	public void beforeMethod() {

		// BrowserSetup.setup("chrome");
		htmlReporter = new ExtentSparkReporter("DeveloperPageReport.html");
		extent = new ExtentReports();
		extent.attachReporter(htmlReporter);
	}

	public void WebSetup() {
		driver.get("http://localhost/CryptoTracker/Aboutcrpy.html");
		DeveloperPage = new DeveloperPage(driver);

	}

	// SC_01_TC_01 (Valid Email and Password)
	@Test(priority = 1)

	public void developerTest() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforDeveloperTest");

		test1 = extent.createTest("DeveloperPage Valid Email and Password", "TestCase1");

		driver.get("http://localhost/CryptoTracker/creator.html");

		DeveloperPage = new DeveloperPage(driver);

		Thread.sleep(2000);

		DeveloperPage.ClickButton(Locators.Home_developer_xpath1);

		test1.pass("Clicked on Developer Button");

		System.out.println("pass");

		Thread.sleep(2000);

		Helper.captureScreenshot(driver, "AfterDeveloperTest");

	}

	// SC_01_TC_02 is editable)


	@Test(priority = 2)

	public void MousHover() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforMouseHover");

		test1 = extent.createTest("DeveloperPage MousHover", "TestCase2");

		DeveloperPage.ClickButton(Locators.Home_developer_xpath1);

		DeveloperPage.mouseHoverOnElement(Locators.Home_heading_xpath1);

		test1.pass("MouseHover on Heading");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Heding_xpath);

		test1.pass("MouseHover on SubHeading");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Search_xpath);

		test1.pass("MouseHover on Search Button");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Developer_xpath);

		test1.pass("MouseHover on Developer Button");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Logout_xpath);

		test1.pass("MouseHover on Logout Button");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Text2_xpath);

		test1.pass("MouseHover on Text");

		DeveloperPage.mouseHoverOnElement(Locators.DP_Image);

		test1.pass("MouseHover on Image");

		Helper.captureScreenshot(driver, "AfterMouseHover");

	}

	@Test(priority = 3)

	public void AssertText() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforeAssertText");

		test1 = extent.createTest("DeveloperPage AssertText", "TestCase3");

		DeveloperPage.ClickButton(Locators.Home_developer_xpath1);

		test1.pass("Clicked on Home Page");

		DeveloperPage.AssertGetText(Locators.DP_Heding_xpath, "Crypto Currency");

		test1.pass("Heading Asserted Text");

		DeveloperPage.AssertGetText(Locators.DP_Search_xpath, "SEARCH");

		test1.pass("Search Button Asserted");

		DeveloperPage.AssertGetText(Locators.DP_Developer_xpath, "DEVELOPER");

		test1.pass("Developer Button Asserted");

		DeveloperPage.AssertGetText(Locators.DP_Logout_xpath, "LOGOUT");

		test1.pass("Logout Button Asserted");

		DeveloperPage.AssertGetText(Locators.DP_Text2_xpath, "Developers & Designers");

		test1.pass("SubHeading Asserted Text");

		Helper.captureScreenshot(driver, "AfterAssertText");

	}

	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}

}
