package com.TestCases;

import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

//import com.Pages.DeveloperPage;
//import com.Pages.LoginPage;
import com.Pages.SearchPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.Utility;
import com.baseClass.Helper;
import com.baseClass.Locators;

public class SearchPageTest {
	SearchPage SearchPage;
	Utility utils = new Utility();
	WebDriver driver = utils.setup();
	Locators Locators = new Locators();

	static ExtentSparkReporter htmlReporter;
	static ExtentReports extent;
	static ExtentTest test1;

	@BeforeTest
	public void beforeMethod() {

		// BrowserSetup.setup("chrome");
		htmlReporter = new ExtentSparkReporter("SearchPageReport.html");
		extent = new ExtentReports();
		extent.attachReporter(htmlReporter);
	}

	public void WebSetup() {
		driver.get("http://localhost/CryptoTracker/Aboutcrpy.html");
		SearchPage = new SearchPage(driver);

	}
	

	// SC_01_TC_01 (assert heading text)

	@Test(priority=1) 

	public void AssertText() throws Exception { 

		WebSetup(); 

		Helper.captureScreenshot(driver, "Before Heading Asserted-SEARCHPAGE"); 

		test1 = extent.createTest("SearchPage AssertText", "TestCase5"); 

		SearchPage.ClickButton(Locators.Home_search_xpath1); 

		test1.pass("Click on Search Button"); 

		SearchPage.AssertGetText(Locators.SP_heading_xpath,"Real Time Crypto Tracker"); 

		test1.pass(" Real Time Crypto Tracker "); 

		Helper.captureScreenshot(driver, "After Heading Asserted-SEARCHPAGE"); 


	}

	// SC_01_TC_02 (search field editable)

	@Test(priority = 2)

	public void Editable() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "Before search field editable ");

		test1 = extent.createTest("Searchpage Editable", "TestCase2");

		SearchPage.ClickButton(Locators.Home_search_xpath1);

		test1.pass("Click on Search Button");

		SearchPage.fieldEditable(Locators.SP_SearchBox_xpath);

		test1.pass("SearchBox is editable");

		Helper.captureScreenshot(driver, "After search field editable ");

	}

	// SC_01_TC_02 (mouse Hover )

	@Test(priority = 3)

	public void MouseHover() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforMouseHover");

		test1 = extent.createTest("SearchPage MouseHover", "TestCase2");

		SearchPage.ClickButton(Locators.Home_search_xpath1);

		test1.pass("Clicked on Search Button");

		SearchPage.mouseHoverOnElement(Locators.SP_ADX_xpath2);

		test1.pass("Mouse Hover on ADX Text");

	}

	// SC_01_TC_03 (Valid Email and Password)

	@Test(priority = 4)

	public void SearchTest() throws Exception {

		WebSetup();

		Helper.captureScreenshot(driver, "BeforSearchTest");

		test1 = extent.createTest("SearchPage SearchTest", "TestCase4");

		SearchPage.ClickButton(Locators.Home_search_xpath1);

		test1.pass("Clicked on Search Button");

		Thread.sleep(2000);

		SearchPage.ClickButton(Locators.SP_ADX_text);

		test1.pass("Clicked on ADX Text");

		Helper.captureScreenshot(driver, "After search Test ");

	}

	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}

}
