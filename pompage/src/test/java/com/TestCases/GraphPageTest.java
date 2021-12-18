package com.TestCases;

import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

import com.Pages.HomePage;
import com.Pages.LoginPage;
import com.Pages.SearchPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import com.baseClass.Helper;
import com.baseClass.Locators;
import com.baseClass.Utility;
import com.Pages.*;

public class GraphPageTest extends Utility {

	private static final String priority = null;
	HomePage homePage;
	SearchPage SearchPage;
	GraphPage GraphPage;
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
		htmlReporter = new ExtentSparkReporter("GraphPageReport.html");
		extent = new ExtentReports();
		extent.attachReporter(htmlReporter);
	}

	public void WebSetup() {
		driver.get("https://crypto-tracker.swapnilg4u.repl.co/");
		GraphPage = new GraphPage(driver);

	}

	// SC_01_TC_01 (assert footer text)
	@Test(priority = 1)
	public void AssertText() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforGraphPage AsserText");

		test1 = extent.createTest("Graph Page AssertText", "TestCase1");
		
		GraphPage.ClickButton(Locators.SP_ADX_text);
		
		Dimension dm = new Dimension(900, 1000);
		driver.manage().window().setSize(dm);
		Thread.sleep(2000);
		
		GraphPage.AssertGetText(Locators.GP_footer_id, "Made with in India by Swapnil");
		test1.pass("assert footer text");
		Helper.captureScreenshot(driver, "BeforGraphPage AsserText");

	}

	// SC_01_TC_02 (assert Drak mode button)
	@Test(priority = 2)
	public void clickButton() throws Exception {
		WebSetup();
		Helper.captureScreenshot(driver, "BeforGraphPage clickButtont");
		test1 = extent.createTest("Drak mode button", "TestCase2");
		GraphPage.ClickButton(Locators.SP_ADX_text);
		
		Dimension dm = new Dimension(900, 1000);
		driver.manage().window().setSize(dm);
		Thread.sleep(2000);
		
		GraphPage.ClickButton(Locators.GP_button_xpath);
		test1.pass("Click button dark mode");
		Helper.captureScreenshot(driver, "AfterGraphPage clickButtont");
	}

	@AfterTest
	public void TrarDown() {
		extent.flush();
		driver.quit();
	}

}
