package com.Pages;

import static org.testng.Assert.assertTrue;

import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.baseClass.BaseClass;
import com.baseClass.ConfigFileReader;
import com.baseClass.Locators;
import com.baseClass.Utility;

public class RegisterPage extends Utility {
	WebDriver driver;
	ConfigFileReader ConfigFileReader;
	Locators Locators;

	// @FindBy(id = "email")
	// @CacheLookup
	// public WebElement Email;
	//
	// @FindBy(id = "pass")
	// WebElement Password;
	//
	// @FindBy(id = "login")
	// WebElement Login;
	public RegisterPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
		objConfigFileReader = new ConfigFileReader();
		Locators = new Locators();
	}

	public HomePage fun_register(String Name, String UName, String email, String Num, String password) {
		setName(Name);
		setUName(UName);
		setEmail(email);
		setNum(Num);
		setPassword(password);
		ClickButton(Locators.RP_submitbutton_id);
		return new HomePage(driver);

	}

	public void setName(String Name) {
		getWebElement(Locators.RP_name_id).sendKeys(Name);

	}

	public void setUName(String UName) {
		getWebElement(Locators.RP_uname_id).sendKeys(UName);

	}

	public void setEmail(String Email) {
		getWebElement(Locators.RP_email_id).sendKeys(Email);

	}

	public void setNum(String Num) {
		getWebElement(Locators.RP_number_id).sendKeys(Num);

	}

	public void setPassword(String Password) {
		getWebElement(Locators.RP_password_id).sendKeys(Password);

	}

	// ClickButton
	public void ClickButton(By elementName) {
		getWebElement(elementName).click();
	}

	// get WebElement
	public WebElement getWebElement(By elementName) {
		return driver.findElement(elementName);
	}

	// element Present
	public void elementPresent(By elementname) {
		List<WebElement> elements = driver.findElements(elementname);
		assert (elements.size() > 0);
	}

	// editable textbox
	public void fieldEditable(By elementName) {
		WebElement element = driver.findElement(elementName);
		Boolean isEditable = element.isEnabled() && element.getAttribute("readonly") == null;
		assertTrue(isEditable);
	}

}
