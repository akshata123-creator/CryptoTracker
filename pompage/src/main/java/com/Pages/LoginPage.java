package com.Pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import static org.junit.Assert.assertThat;
import static org.testng.Assert.assertTrue;
import static org.hamcrest.CoreMatchers.is;
import java.util.List;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import com.baseClass.BaseClass;
import com.baseClass.ConfigFileReader;
import com.baseClass.Helper;
import com.baseClass.Locators;
import com.baseClass.Utility;

public class LoginPage extends Utility {
	WebDriver driver;
	ConfigFileReader ConfigFileReader;
	Locators Locators;
	@FindBy(id = "email")
	@CacheLookup
	public WebElement Email;

	@FindBy(id = "pass")
	WebElement Password;

	@FindBy(id = "login")
	WebElement Login;
	
	//constructor
	public LoginPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	    objConfigFileReader = new ConfigFileReader();
	    Locators=new Locators();
	}
	
	public String getLoginPageTitle() {
        return driver.getTitle();
    }
    public void assertLoginTitle(){
       objConfigFileReader = new ConfigFileReader();
        assertThat(getLoginPageTitle(), is(objConfigFileReader.getString("LoginTitle")));
        {
            WebDriverWait wait = new WebDriverWait(driver, 15);          
            wait.until(ExpectedConditions.presenceOfElementLocated(Locators.LP_signupbutton_css));
        }
    }
    
    
	
	// login function
	public HomePage fun_login(String email, String password) {
		setEmail(email);
		setPassword(password);
		Helper.captureScreenshot(driver, "AfterLoginloginTest");
		clickLogin();
		return new HomePage(driver);

	}

	// set email
	public void setEmail(String Email1) {
		Email.sendKeys(Email1);
	}

	// set password
	public void setPassword(String Password1) {
		Password.sendKeys(Password1);
	}

	public void clickLogin() {
		Login.click();
	}

	// ClickButton
	public void ClickButton(By elementName) {
		getWebElement(elementName).click();
	}

	// get WebElement
	public WebElement getWebElement(By elementName) {
		return driver.findElement(elementName);
	}

	// Hover mouse on the element
	public void mouseHoverOnElement(By elementName) {
		WebElement element = getWebElement(elementName);
		Actions builder = new Actions(driver);
		builder.moveToElement(element).perform();
	}

	// Assert Get Text
	public void AssertGetText(By elementName, String stringName) {
		assertThat(getWebElement(elementName).getText(), is(objConfigFileReader.getString(stringName)));
	}

	// Get CSS property in String Format
	public String VerifyCssProperty(By elementName, String propertyName) {
		String cssPropertyText = getWebElement(elementName).getCssValue(objConfigFileReader.getString(propertyName));
		return cssPropertyText;
	}

	// editable textbox
	public void fieldEditable(By elementName) {
		WebElement element = driver.findElement(elementName);
		Boolean isEditable = element.isEnabled() && element.getAttribute("readonly") == null;
		assertTrue(isEditable);
	}

//	public void assertHomeTitle() {
//		
//		
//	}

}
