// Importing the necessary libraries
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace Spring_2025_CS411_2 {

    /// <summary>

    /// </summary>
    

    public partial class MainWindow : Window
    {
        public MainWindow() {
            InitializeComponent();
        }

        private void ConvertButton_Click(object sender, RoutedEventArgs e) {
            try {
                string user_input = FahrenheitTextBox.Text;
                double fahrenheit = double.Parse(user_input);
                double celsius = (fahrenheit - 32) * 5 / 9;
                ResultLabel.Text = $"Result: {celsius:F2} °C";
            }

            catch (FormatException) {
                MessageBox.Show("Please enter a valid number!", 
                "Invalid Input", MessageBoxButton.OK, MessageBoxImage.Warning);
            }
        }
    }
}