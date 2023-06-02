<?php
require_once('include.php');


if(!isset($_SESSION['admin']['ok']) || !$_SESSION['admin']['admin_acceuil']){
   header('Location: /erreur/erreur.php');
}



   $DBB = new connexionDB();-
   

   $req = $DBB->prepare("SELECT u.*, ar.libelle
   FROM utilisateur u
   LEFT JOIN admin_role ar ON ar.role = u.role
   WHERE u.id <> ?
   ORDER BY ar.ordre, u.pseudo");
   
   $see_tchat = $DB->query("SELECT t.*, u.pseudo 
      FROM tchat t
      LEFT JOIN utilisateur u ON u.id = t.id_pseudo
      ORDER BY date_message
      LIMIT 100");
 
   $see_tchat = $see_tchat->fetchAll();

   // load mess
 
   if(isset($_GET['id'])){
 
      $id = (int) $_GET['id'];
 
      $see_tchat = $DB->query("SELECT t.*, u.pseudo 
         FROM tchat t
         LEFT JOIN utilisateur u ON u.id = t.id_pseudo
         WHERE t.id 
         ORDER BY date_message", 
         array($id));
 
      $see_tchat = $see_tchat->fetchAll();
 
      if (count($see_tchat) > 0){
 
         foreach($see_tchat as $st){
 
            $date_message = date_create($st['date_message']);
            $date_message = date_format($date_message, 'd M Y à H:i:s');
 
            if(isset($_SESSION['id']) && $st['id_pseudo'] == $_SESSION['id']){
               ?><div style="float: right;width: auto; max-width: 80%; margin-right: 26px;position: relative;padding: 7px 20px;color: #fff;background: #0B93F6;border-radius: 5px;margin-bottom: 15px; clear: both">
 
                     <span id="<?= $st['id'] ?>"><?= nl2br($st['message']) ?></span>
 
                     <div style="font-size: 10px; text-align: right; margin-top: 10px">Par <?= $st['pseudo'] ?>, le <?= $date_message ?></div></div><?php
            }else{
               ?><div style="position: relative;padding: 7px 20px;background: #E5E5EA;border-radius: 5px;color: #000;float: left;width: auto; max-width: 80%; margin-left: 10px;margin-bottom: 15px; clear: both">
 
                     <span id="<?= $st['id'] ?>"><?= nl2br($st['message']) ?></span>
 
                     <div style="font-size: 10px; text-align: right; margin-top: 10px">Par <?= $st['pseudo'] ?>, le <?= $date_message ?></div></div><?php
            }   
         }
         ?>
         
         <script>document.getElementById('msg').scrollTop = document.getElementById('msg').scrollHeight;</script>   
      <?php
      }
   }

   // send mess $_GET

   if(isset($_SESSION['id'])){ 
 
      $mess = htmlspecialchars(trim($_POST['message']));
 
      if(isset($mess) && !isset($mess)){
 
         $verif_user = $BDD->query("SELECT id FROM utilisateur WHERE id = ?",
            array($_SESSION['id']));
 
         $verif_user = $verif_user->fetch();
 
         if(isset($verif_user['id'])){
 
            $date_message = date('Y-m-d H:i:s');
 
            $BDD->insert("INSERT INTO tchat (id_pseudo, message, date_message) VALUES (?, ?, ?)",
               array($_SESSION['id'], $mess, $date_message));
 
            $lastID = $BDD->query("SELECT id FROM tchat WHERE id_pseudo = ? ORDER BY date_message DESC LIMIT 1", 
               array($_SESSION['id']));
 
            $lastID = $lastID->fetch();
 
            $date_message = date_create($date_message);
            $date_message = date_format($date_message, 'd M Y à H:i:s');
 
            ?><div style="float: right;width: auto; max-width: 80%; margin-right: 26px;position: relative;padding: 7px 20px;color: #fff;background: #0B93F6;border-radius: 5px;margin-bottom: 15px; clear: both"><span id="<?= $lastID['id'] ?>"><?= nl2br($mess) ?></span>               
                  <div style="font-size: 10px; text-align: right; margin-top: 10px">Par <?= $_SESSION['pseudo'] ?>, le <?= $date_message ?></div></div>
 
               <script>document.getElementById('msg').scrollTop = document.getElementById('msg').scrollHeight;
               </script><?php
 
         }
      }      
   }


?>

<!DOCTYPE html>
<html>
<head>
<?php
   require_once('./_head/meta.php');

   require_once('./_head/script.php');

   require_once('./_head/link.php');

?>
<script src="//code.jquery.com/jquery-1.12.0.min.js">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="folder_name/jquery-1.12.0.js"></script>
<title>Chat</title>
<link href="css/jquery-ui.structure.min.css" rel="stylesheet" type="text/css"/>
<link href="css/jquery-ui.min.css" rel="stylesheet" type="text/css"/>
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css">
<link href="css/style.css" rel="stylesheet" type="text/css"/>
 
 
   
 
   <body>

   <style> body{background-color: #1F1D2B;}</style>

   <header>
            <?php
                require_once('_header/header_admin.php')
            ?>
    </header>

      <div class="container" style=" margin-top: 20vh;">      
         <div class="row"><div class="col-xs-12 col-sm-12 col-md-12">
            <div style="background: white; border-radius: 10px; box-shadow: 0 0 15px rgba(0, 0, 0, 0.1); padding: 10px  margin-top: 20vh;">
               <div style="font-size: 24px; font-weight: bold">Tchat</div>
                  <div id="msg" style="border: 1px solid #cccccc; padding: 10px 0; border-radius: 5px;overflow: scroll;height: 400px;margin: 10px 0; background: white"><?php   
 
                        foreach($see_tchat as $st){    
 
                           $date_message = date_create($st['date_message']);
                           $date_message = date_format($date_message, 'd M Y à H:i:s');
 
                           if(isset($_SESSION['id']) && $st['id_pseudo'] == $_SESSION['id']){
                        ?>
                        <div style="float: right;width: auto; max-width: 80%; margin-right: 26px;position: relative;padding: 7px 20px;color: #fff;background: #0B93F6;border-radius: 5px;margin-bottom: 15px; clear: both">
 
                              <span id="<?= $st['id'] ?>"><?= nl2br($st['message']) ?></span>
 
                              <div style="font-size: 10px; text-align: right; margin-top: 10px">Par <?= $st['pseudo'] ?>, le <?= $date_message ?></div></div><?php
                           }else{
                        ?><div style="position: relative;padding: 7px 20px;background: #E5E5EA;border-radius: 5px;color: #000;float: left;width: auto; max-width: 80%; margin-left: 10px;margin-bottom: 15px; clear: both">
 
                              <span id="<?= $st['id'] ?>"><?= nl2br($st['message']) ?></span>
 
                              <div style="font-size: 10px; text-align: right; margin-top: 10px">Par <?= $st['pseudo'] ?>, le <?= $date_message ?></div></div><?php
                           }
                        }   
                     ?>
                  <div id="message_recept"></div>                  
               </div>
 
                  <?php 
                  if(isset($_SESSION['id'])){ 
                  ?>
                     <div style="border: 1px solid #cccccc; border-radius: 5px; position: relative; padding-top: 5px; background: white">
                     <form method="get" name="message">
                              <textarea value="<?php if(isset($message))?>" class="autoExpand" rows="1" data-min-rows="1" name="message" id="message" class="msg" placeholder="Envoyer votre message" style="border: none;overflow: none; resize: none; width: 90%; outline: none; padding: 0 5px"></textarea>
                           <div style="position: absolute;top: -5px;right: 2px;font-size: 28px;">
                           <button type="submit" name="message" id="message" class="formbtn">Envoyer</button>
                              <style> body{background-color: #1F1D2B;}button{background-color: #6E40F3;border: 2px solid #6E40F3;border-radius: 4px;color: #fff;cursor: pointer;display: block;font-family: inherit;font-size: 16px;padding: 10px;margin-top: 20px;width: 100%;}</style>
                           </div>      
                     </form>   
                  </div>
                  <?php
                      }       
                   ?>
               </div>
            </div>
         </div>
      </div>
 
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
      <script src="https://code.jquery.com/jquery-1.12.4.js"></script><script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
      <script src="js/bootstrap.min.js"></script>
      <script type="text/javascript">         
         var isopen = false;
 
         function openNav(x) {
 
            if(!isopen){
               isopen = !isopen;
               document.getElementById("myNav").style.height = "100%";
               x.classList.toggle("change");
            }else{
               isopen = !isopen;
               document.getElementById("myNav").style.height = "0%";
               x.classList.toggle("change");
            }
 
         }
 
         document.getElementById('msg').scrollTop = document.getElementById('msg').scrollHeight;      
 
         $('#envoi').click(function(e){
            e.preventDefault();
 
            var message = encodeURIComponent($('#message').val());
 
            message = message.trim();
 
            $('#message').val(null);
 
            if(message != ""){
                $.ajax({
                   url : 'function/send_mess.php?message=' + message,
                  type : 'GET',
                  dataType : "html",
                  success : function(data){
                       $("#message_recept").append(data);
                  }
                });
            }
         });
 
         setInterval("load_mess()", 1000);
 
           function load_mess(){  
 
              var lastID = $('#msg span:last').attr('id');
 
              if(lastID > 0){          
               $.ajax({
                  url : 'function/load_mess.php?id=' + lastID,
                  type : 'GET',
                  dataType : "html",
                  success : function(data){
                     $("#message_recept").append(data);
                  },
                  error : function(){
                     //alert("Oops une erreur est survenue lors du chargement du message !");
                  }
               });
            }
         };
 
         $(document).one('focus.autoExpand', 'textarea.autoExpand', function(){
             var savedValue = this.value;
             this.value = '';
             this.baseScrollHeight = this.scrollHeight;
             this.value = savedValue;
 
         }).on('input.autoExpand', 'textarea.autoExpand', function(){
             var minRows = this.getAttribute('data-min-rows')|0, rows;
             this.rows = minRows;
             rows = Math.ceil((this.scrollHeight - this.baseScrollHeight) / 20);
             this.rows = minRows + rows;
         });
      </script>
      </body>
</html>


// This is a PHP script that appears to be a chat application. It first checks whether the user is an admin and has access to the chat application. It then retrieves the chat messages from the database and displays them, with newer messages displayed at the bottom. If a user clicks on a message, it displays that message and any previous messages. Finally, if a user submits a new message, it is added to the database and displayed in the chat.

// However, there are several errors and potential issues with this script:

// On line 22, the variable $DBB is assigned to a new instance of connexionDB, but the class name suggests that it should be named connexionDB instead of DBB.

// On line 25, the $see_tchat variable is assigned the result of a query from $DB, but $DB is not defined anywhere in the script. It is possible that this was meant to be $DBB.

// On line 27, the $see_tchat variable is assigned the result of fetchAll(), but it is not checked whether the query returned any results. If there are no messages in the database, fetchAll() will return an empty array, which could cause issues later on.

// On line 45, the WHERE clause of the SQL query is incomplete. It is missing a comparison to a value, such as WHERE t.id = ?. This could cause a SQL syntax error.

// On line 47, the array($id) argument of the query() function call is unnecessary, as the id value is already being passed in the WHERE clause of the query.

// On line 48, the $see_tchat variable is assigned the result of fetchAll(), but it is not checked whether the query returned any results. If there are no messages with the given ID in the database, fetchAll() will return an empty array, which could cause issues later on.

// On line 64, the $mess variable is assigned the result of htmlspecialchars(trim($_POST['message'])), but the isset() check is incorrect. It should be checking whether $_POST['message'] is set, not whether $mess is set.

// On line 66, the !isset($mess) check is incorrect. It should be checking whether $mess is empty, not whether it is not set.

// On line 75, the $BDD variable is undefined. It is possible that this was meant to be $DBB.

// On line 84, the $lastID variable is assigned the result of fetch(), but it is not checked whether the query returned any results. If there are no messages with the given ID in the database, fetch() will return false, which could cause issues later on.

// On line 88, the $_SESSION['pseudo'] variable is used without checking whether it is set. If the user is not logged in, this will cause a notice to be generated.

// There are several script tags on lines 16-18 that are not closed properly.

// There are several link tags on lines 20-21 that are not closed properly.

// The ellipsis at the end of the file suggest that there may be more code that has been omitted. This could potentially affect the functionality of the script.