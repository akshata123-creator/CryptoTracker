/**
 * 
 */
package com.baseClass;

import java.io.File;
import java.io.IOException;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.ITestResult;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.BeforeSuite;

import com.Pages.LoginPage;
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.MediaEntityBuilder;
//import com.aventstack.extentreports.reporter.ExtentHtmlReporter;

/**
 * @author akshata_chaudhari
 *
 */
public class BaseClass {
	public WebDriver driver;

	/*
	 * @AfterMethod public void captureScreenshot(ITestResult result) { if
	 * (result.getStatus() == ITestResult.FAILURE) { //
	 * Helper.captureScreenshot(driver,result.getName()); try {
	 * logger.fail("Test Failed", MediaEntityBuilder
	 * .createScreenCaptureFromPath(Helper.captureScreenshot(driver,
	 * result.getName())).build()); } catch (IOException e) { e.printStackTrace(); }
	 * } else if (result.getStatus() == ITestResult.SUCCESS) { try {
	 * logger.pass(result.getName() + "Passed", MediaEntityBuilder
	 * .createScreenCaptureFromPath(Helper.captureScreenshot(driver,
	 * result.getName())).build()); } catch (IOException e) { e.printStackTrace(); }
	 * 
	 * }
	 * 
	 * report.flush(); }
	 */
	 //report.flush();
}
