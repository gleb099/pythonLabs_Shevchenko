using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WorkWithSheets_2
{
    public partial class Form1 : Form
    {
        private GoogleHelper helper;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string token = "Вставляем сюда свой код";
            string sheetFileName = "TestSheet";
            this.helper = new GoogleHelper(token, sheetFileName);

            bool success = this.helper.Start().Result;
            if (success)
            {
                button2.Enabled = true;
                button3.Enabled = true;
            }
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.helper.Set(cellName: txtCellNameSet.Text, value: txtCellValue.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            var result = this.helper.Get(cellName: txtCellNameSet.Text);
            txtCellGetValue.Text = result;
        }
    }
}
