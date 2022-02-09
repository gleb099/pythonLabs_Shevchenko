namespace WorkWithSheets_2
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.txtCellNameSet = new System.Windows.Forms.TextBox();
            this.txtCellGetValue = new System.Windows.Forms.TextBox();
            this.txtCellValue = new System.Windows.Forms.TextBox();
            this.txtCellNameGet = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(123, 55);
            this.button1.TabIndex = 0;
            this.button1.Text = "Start";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Enabled = false;
            this.button2.Location = new System.Drawing.Point(270, 69);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(123, 55);
            this.button2.TabIndex = 1;
            this.button2.Text = "Set";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Enabled = false;
            this.button3.Location = new System.Drawing.Point(141, 147);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(123, 55);
            this.button3.TabIndex = 2;
            this.button3.Text = "Get";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // txtCellNameSet
            // 
            this.txtCellNameSet.Location = new System.Drawing.Point(12, 85);
            this.txtCellNameSet.Name = "txtCellNameSet";
            this.txtCellNameSet.Size = new System.Drawing.Size(123, 22);
            this.txtCellNameSet.TabIndex = 3;
            // 
            // txtCellGetValue
            // 
            this.txtCellGetValue.Location = new System.Drawing.Point(270, 163);
            this.txtCellGetValue.Name = "txtCellGetValue";
            this.txtCellGetValue.Size = new System.Drawing.Size(123, 22);
            this.txtCellGetValue.TabIndex = 4;
            // 
            // txtCellValue
            // 
            this.txtCellValue.Location = new System.Drawing.Point(141, 85);
            this.txtCellValue.Name = "txtCellValue";
            this.txtCellValue.Size = new System.Drawing.Size(123, 22);
            this.txtCellValue.TabIndex = 5;
            // 
            // txtCellNameGet
            // 
            this.txtCellNameGet.Location = new System.Drawing.Point(12, 163);
            this.txtCellNameGet.Name = "txtCellNameGet";
            this.txtCellNameGet.Size = new System.Drawing.Size(123, 22);
            this.txtCellNameGet.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(414, 231);
            this.Controls.Add(this.txtCellNameGet);
            this.Controls.Add(this.txtCellValue);
            this.Controls.Add(this.txtCellGetValue);
            this.Controls.Add(this.txtCellNameSet);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "TestApp";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TextBox txtCellNameSet;
        private System.Windows.Forms.TextBox txtCellGetValue;
        private System.Windows.Forms.TextBox txtCellValue;
        private System.Windows.Forms.TextBox txtCellNameGet;
    }
}

